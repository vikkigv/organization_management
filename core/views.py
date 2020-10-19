from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_datatables.pagination import DatatablesLimitOffsetPagination
from .serializers import *
from .models import *


# Create your views here.

class PaginationList(DatatablesLimitOffsetPagination):
    PAGE_SIZE = 10


class CompanyView(APIView):
    serializer_class = CompanySerializer

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Company Added Successfully"})


class CompanyViewWithId(APIView):
    serializer_class = CompanySerializer

    def get(self, request, pk):
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(company)
        return Response({'data': serializer.data})

    def put(self, request, pk):
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Company Updated Successfully"})

    def delete(self, request, pk):
        company = Company.objects.get(id=pk)
        company.delete()
        return Response({'success': 'Company Deleted Successfully'})


class EmployeeView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    pagination_class = PaginationList

    def get_queryset(self):
        queryset = Employee.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
            return queryset
        else:
            return queryset

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Employee Added Successfully"})


class EmployeeViewWithId(APIView):
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee)
        return Response({'data': serializer.data})

    def put(self, request, pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Employee Updated Successfully"})

    def delete(self, request, pk):
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return Response({'success': 'Employee Deleted Successfully'})
