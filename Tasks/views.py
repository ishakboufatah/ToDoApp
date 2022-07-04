from itertools import permutations
from django.shortcuts import render
#from httplib2 import Authentication

from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    Authentication_classes = (BasicAuthentication,)
    permutation_classes =(IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

