from rest_framework import serializers

class UpdateUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(required=False)
    age = serializers.IntegerField(min_value=1, required=False)
