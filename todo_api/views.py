from rest_framework.viewsets import ModelViewSet
from django.utils.module_loading import import_string

from todo_api.settings import api_settings
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [import_string(permission_class) for permission_class in api_settings.TASK_PERMISSIONS]

# Create your views here.
