from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from utils.utility import CustomGetObjectMixin, SuccessResponseMixin

class TaskListCreateView(SuccessResponseMixin,generics.ListCreateAPIView):
    datakey = success_key = "task"
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class TaskDetailView(SuccessResponseMixin, CustomGetObjectMixin, generics.RetrieveUpdateDestroyAPIView):
    success_key = "task"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
