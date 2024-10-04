from django.db.models import Count
from rest_framework import serializers
from .models import Employee, Organization
from django.db.models import Count


class OrganizationSerializer(serializers.ModelSerializer):
     class Meta:
          model = Organization
          fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
     class Meta:
          model = Employee
          fields = ['id', 'name', 'salary', 'incentives', 'organization']
     incentives = serializers.SerializerMethodField(method_name='bonus')
     def bonus(self, employee:Employee):
               return employee.salary + 3000
