from rest_framework import serializers

from web.models import User, Group, GroupParticipant


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'city', 'gender', 'birthday', 'description', 'created_at', 'image']


class UserInGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupParticipant
        fields = ['role', 'user']


class GroupSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'title', 'city', 'description', 'created_at', 'updated_at', 'users']

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

    class Meta:
        model = Group
        fields = ['id', 'title', 'city', 'description', 'created_at', 'updated_at', 'users']

    def create(self, validated_data):
        group_participant = validated_data.pop('users')
        group = Group.objects.create(**validated_data)
        for gp in group_participant:
            user = gp.pop('user')
            GroupParticipant.objects.create(**gp, user=user, group=group)
        return group
