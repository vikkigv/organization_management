from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


# Create your views here.


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


class EmployeeView(APIView):
    serializer_class = EmployeeSerializer

    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
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
