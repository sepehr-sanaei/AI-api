from rest_framework import serializers

class AISerializer(serializers.Serializer):
    """
    Serializer for AI model data.
    """
    free_hours = serializers.IntegerField(min_value=1)
    lessons = serializers.DictField(
        child=serializers.IntegerField(min_value=1)
    )