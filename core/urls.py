from django.urls import path
from core import views

urlpatterns = [
    path('companyview/', views.CompanyView.as_view(), name='company view'),
    path('companyview/<int:pk>', views.CompanyViewWithId.as_view(), name='company view with id'),
    path('employeeview/', views.EmployeeView.as_view(), name='employee view'),
    path('employeeview/<int:pk>', views.EmployeeViewWithId.as_view(), name='employee view with id'),
]
