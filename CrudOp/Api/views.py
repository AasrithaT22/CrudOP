from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Organization
from .serializers import EmployeeSerializer, OrganizationSerializer
# Create your views here.

class EmployeeList(APIView):
    def get(self, request):
        cache_key = f"employee{request.get_full_path()}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
        queryset = Employee.objects.select_related('organization').all()
        # df = pd.DataFrame(list(queryset.values()))
        # df['Formated_Salary'] = df['salary'].map('${:,.2f}'.format)
        paginator = PageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = EmployeeSerializer(paginated_queryset, many=True)
        paginated_response = paginator.get_paginated_response(serializer.data)
        cache.set(cache_key, paginated_response.data, timeout=60*3)
        return paginated_response

        # queryset = Employee.objects.select_related('organization').all()
        # paginator = PageNumberPagination()
        # paginated_queryset = paginator.paginate_queryset(queryset, request)
        # serializer = EmployeeSerializer(paginated_queryset, many=True)
        # return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EmployeeDetail(APIView):
    def get(self, request, pk):
        if cache.get(pk):
            employee = cache.get(pk)
        else:
            employee = get_object_or_404(Employee, pk=pk)
            cache.set(pk, employee, timeout=60*3)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def patch(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response({'message':'Employee has been successfully deleted.'},status=status.HTTP_204_NO_CONTENT)

class OrganizationList(APIView):
    def get(self, request):
        cache_key = f"organization{request.get_full_path()}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
        queryset = Organization.objects.all()
        paginator = LimitOffsetPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = OrganizationSerializer(paginated_queryset, many=True)
        paginated_response = paginator.get_paginated_response(serializer.data)
        cache.set(cache_key, paginated_response, timeout=60*3)
        return paginated_response

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrganizationDetail(APIView):
    def get(self, request, pk):
        if cache.get(pk):
            organization = cache.get(pk)
        else:
            organization = get_object_or_404(Organization, pk=pk)
            cache.set(pk, organization, timeout=60*3)
        serializer = OrganizationSerializer (organization)
        return Response(serializer.data)
    def put(self, request, pk):
        organization = get_object_or_404(Organization, pk=pk)
        serializer = OrganizationSerializer(organization, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def patch(self, request, pk):
        organization = get_object_or_404(Organization, pk=pk)
        serializer = OrganizationSerializer(organization, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self):
        organization = get_object_or_404(Organization, pk=id)
        organization.delete()
        return Response({'message':'deleted'}, status=status.HTTP_204_NO_CONTENT)
