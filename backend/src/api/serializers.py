from rest_framework import serializers

from web.models import User, Group


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'city']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User.objects.create_user(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            city=self.validated_data['city'],
        )

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'city',
                  'gender', 'birthday', 'description', 'created_at', 'image']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'title', 'city', 'description', 'created_at', 'updated_at']
