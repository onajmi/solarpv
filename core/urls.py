from django.urls import path
from .views import index, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('product'), product, name='product')
    path('client'), client, name='client')
    path('certificate'), certificate, name='certificate')
    path('location'), location, name='location')
    path('test_standard'), test_standard, name='test_standard')
]
