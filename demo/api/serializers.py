from rest_framework import serializers
from .models import Result


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ['id', 'output']
        read_only_fields = ['id', 'output']

    """
    id = serializers.UUIDField(read_only=True, default=uuid.uuid4)
    output = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        self.output = validated_data.get('output')
        return self
    """
