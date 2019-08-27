from rest_framework import viewsets
from rest_framework import mixins
from .models import Result
from .serializers import ResultSerializer
from . import tasks


class ResultViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):

    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def perform_create(self, serializer):
        pk = serializer.validated_data.get('id')
        x = serializer.validated_data.pop('x')
        y = serializer.validated_data.pop('y')
        r = tasks.add.delay(pk, x, y)
        serializer.save(task_id=r.id)
