from django.shortcuts import get_object_or_404
from rest_framework import serializers

from web.models import User, Group, GroupParticipant, Category, MeetingParticipant, Meeting


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'city', 'gender', 'birthday', 'description', 'created_at', 'image']


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["old_password", "new_password"]

    def validate_old_password(self, password):
        user = self.context['request'].user
        if not user.check_password(password):
            raise serializers.ValidationError("Текущий пароль введен неправильно. Попробуйте еще раз")
        return password

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class UserInGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupParticipant
        fields = ['role', 'user']


class GroupSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'title', 'city', 'description', 'created_at', 'updated_at', 'users', 'categories']

    def get_users(self, instance):
        group_participants = GroupParticipant.objects.filter(group=instance)
        return [UserInGroupSerializer(user).data for user in group_participants]


class UserInGroupRoleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, source='user', queryset=User.objects.all())

    class Meta:
        model = GroupParticipant
        fields = ['user', 'user_id', 'role']


class GroupCreateSerializer(serializers.ModelSerializer):
    users = UserInGroupRoleSerializer(many=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'title', 'city', 'description', 'created_at', 'updated_at', 'categories', 'users']

    def create(self, validated_data):
        group_participant = validated_data.pop('users')
        group = Group.objects.create(**validated_data)
        group.categories.set(self.context["request"].data.get('categories'))
        for gp in group_participant:
            user = gp.pop('user')
            GroupParticipant.objects.create(**gp, user=user, group=group)
        return group


class GroupUpdateSerializer(serializers.ModelSerializer):
    users = UserInGroupRoleSerializer(many=True)
    # categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'title', 'city', 'description', 'created_at', 'updated_at', 'users']

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.city = validated_data.get("city", instance.city)
        instance.description = validated_data.get("description", instance.description)
        instance.categories.set(validated_data.get('categories', []))
        users = validated_data.pop('users', [])
        if len(users) > 0:
            GroupParticipant.objects.create(role=users[0].pop('role'), user=users[0].pop('user'), group=instance)
        instance.save()
        return instance


class GroupParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupParticipant
        fields = "__all__"


class UserInMeetingRoleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, source='user', queryset=User.objects.all())

    class Meta:
        model = MeetingParticipant
        fields = ['user', 'user_id', 'role']


class MeetingChangeSerializer(serializers.ModelSerializer):
    users = UserInMeetingRoleSerializer(many=True)
    group_id = serializers.PrimaryKeyRelatedField(write_only=True, source='group', queryset=Group.objects.all())

    class Meta:
        model = Meeting
        fields = ['id', 'title', 'location', 'description', 'is_online', 'date', 'group_id', 'users']

    def create(self, validated_data):
        meeting_participant = validated_data.pop('users')
        meeting = Meeting.objects.create(**validated_data)
        for mp in meeting_participant:
            user = mp.pop('user')
            MeetingParticipant.objects.create(**mp, user=user, meeting=meeting)
        return meeting

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.location = validated_data.get("location", instance.location)
        instance.description = validated_data.get("description", instance.description)
        instance.is_online = validated_data.get("is_online", instance.is_online)
        instance.date = validated_data.get("date", instance.date)
        users = validated_data.pop('users', [])
        if len(users) > 0:
            MeetingParticipant.objects.create(role=users[0].pop('role'), user=users[0].pop('user'), meeting=instance)
        instance.save()
        return instance




class UserInMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeetingParticipant
        fields = ['role', 'user']


class GroupWithoutUser(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'title', 'city']


class MeetingSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()

    class Meta:
        model = Meeting
        fields = "__all__"

    def get_users(self, instance):
        meeting_participants = MeetingParticipant.objects.filter(meeting=instance)
        return [UserInMeetingSerializer(user).data for user in meeting_participants]

    def get_group(self, instance):
        group = get_object_or_404(Group, id=instance.group_id)
        return GroupWithoutUser(group).data


class MeetingParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingParticipant
        fields = "__all__"
