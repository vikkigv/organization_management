from rest_framework import serializers

from core.models import Company, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(queryset=Company.objects.all(), slug_field='org_name')

    class Meta:
        model = Employee
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    employee_details = EmployeeSerializer(many=True, required=False)
    no_of_emp = serializers.SerializerMethodField()

    def get_no_of_emp(self, instance):
        emp = Employee.objects.filter(company_id=instance).count()
        return emp

    class Meta:
        model = Company
        fields = ['org_name', 'location', 'no_of_emp', 'employee_details']
