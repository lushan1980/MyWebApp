from django.urls import URLPattern, path
from pip import main
from .views import customer_corr_view


app_name = 'customers'

urlpatterns = [
    path('', customer_corr_view, name='customer-corr-view'),
]