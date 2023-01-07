
from django.shortcuts import render
from REST_App.models import Employee
from REST_App.serializers import EmployeeModelSerializer

from rest_framework import generics

class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
