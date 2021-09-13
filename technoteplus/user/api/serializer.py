from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserListRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for User List"""
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return "{0} {1}".format(obj.first_name, obj.last_name)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'full_name']


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    """ Validation for creation """

    def validate_first_name(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Firstname Must be included")
        return value

    def validate_last_name(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Lastname Must be included")
        return value

    def validate_password(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Password Must be at lease 5 character length")
        return "hidden"

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'password']
