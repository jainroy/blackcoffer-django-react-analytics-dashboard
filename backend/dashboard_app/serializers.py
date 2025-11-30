from rest_framework import serializers
from .models import InsightEntry


class InsightEntrySerializer(serializers.ModelSerializer):
    """
    Serializer to convert InsightEntry model instances to JSON
    and validate input if needed.
    """

    class Meta:
        model = InsightEntry
        fields = '__all__'
