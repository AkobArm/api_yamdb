from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..api_yamdb.settings import FIELDS

User = get_user_model()


class UserSignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = FIELDS

    def validate(self, value):
        if value == 'me':
            raise serializers.ValidationError('Выберите другое имя')
        return value


class UserSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = FIELDS
        read_only_fields = ('role',)
