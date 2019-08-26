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
        obj = serializer.save()
        r = tasks.add.delay(obj.pk, 2, 2)
        obj = serializer.save(task_id=r.id)
