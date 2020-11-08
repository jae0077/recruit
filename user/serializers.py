from rest_framework import serializers
from user.models import user

class UserSerializer(serializers.Serializer):
    user_type
    user_id
    user_pw
    user_email
    user_name
    user_adress
    created_at
