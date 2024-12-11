from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    @action(detail=False, methods=['get'])
    def by_status(self, request):
        status = request.query_params.get('status', 'PENDING')
        tasks = Task.objects.filter(status=status)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
