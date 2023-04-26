from django.contrib import admin
from django.urls import path, include
from . import views

from .views import *
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='homes'),
    path('about/', HomeView.as_view(template_name='home/about_us.html'), name='about'),
    path('logout/', logoutuser, name='logout'),
    path('search/', search, name='search'),
    path('login/', handleLogin, name='login'),
    path('create/', product_create, name='create'),
    path('add/<int:pk>/', addqty, name='add'),
    path('edit/<int:pk>/',EditProdView.as_view(), name='edit'),
    path('supedit/<int:pk>/',EditSupplierView.as_view(), name='supedit'),
    path('createsupplier/',CreateSupplierView.as_view(), name='create-supplier'),
    path('contact/',CreateContactView.as_view(), name='contact'),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('delete/<int:id>/', views.delete, name='delete'),

    path('company/', CompanyListView.as_view(), name='company-list'),
    path('delete_comp/<str:id>/', views.delete_comp, name='delete_comp'),
    
    path('suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('delete_supp/<str:id>/', views.delete_supp, name='delete_supp'),

    path('sales/', SalesListView.as_view(), name='sales-list'),
    path('delete_sales/<int:id>/', views.delete_sales, name='delete_sales'),

    path('makebill/', views.makebill, name='makebill'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('create/', ProductCreate.as_view(), name='create'),
    path('createemployee/', views.CreateEmployeeView, name='create-employee'),
    path('createpatient/', views.CreatePatientView, name='create-patient'),

    path('empedit/<int:pk>/',EditEmployeeView.as_view(), name='empedit'),
    path('delete_emp/<int:pk>/', views.delete_emp, name='delete_emp'),

    path('patedit/<int:pk>/',EditPatientView.as_view(), name='patedit'),
    path('delete_patient/<str:id>/', views.delete_pat, name='delete_pat'),

    path('employee/', views.employees, name='employee-list'),
    path('patient/', views.patients, name='patient-list'),
    path('invoice/', views.invoice, name='invoice'),

    path('supplier_invoice/', views.supplier_invoice, name='supplier-invoice'),
    path('delete_supp_inv/<str:id>/', views.delete_supp_inv, name='delete_supp_inv'),

    path('add_supplier_invoice/', views.add_supplier_invoice, name='add-supplier-invoice'),
]