import uuid
from rest_framework import serializers
from .models import Result


class ResultSerializer(serializers.ModelSerializer):

    id = serializers.HiddenField(default=uuid.uuid4)
    x = serializers.IntegerField(write_only=True)
    y = serializers.IntegerField(write_only=True)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.pk
        return ret

    class Meta:
        model = Result
        fields = ['id', 'x', 'y', 'output']
        read_only_fields = ['output']
