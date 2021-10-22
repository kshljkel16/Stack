from rest_framework import serializers
from .models import CustomUser
from .utils import send_activation_code


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length=4, required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
            'password_confirm'
        )
    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            msg_ = (
                'Passwords do not match'
            )
            raise serializers.ValidationError(
                msg_
            )
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        send_activation_code(
            user.email, user.activation_code
        )
        return user