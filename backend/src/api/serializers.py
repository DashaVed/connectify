from rest_framework import serializers

from web.models import User, Group


class RegistrationSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'city']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            name=self.validated_data['name'],
            city=self.validated_data['city'],
        )
        password = self.validated_data['password']
        re_password = self.validated_data['re_password']

        if password != re_password:
            raise serializers.ValidationError({'message': 'Пароли не совпадают'})
        user.set_password(password)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'city', 'gender', 'birthday', 'description', 'created_at', 'image']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'title', 'city', 'description', 'created_at', 'updated_at']
