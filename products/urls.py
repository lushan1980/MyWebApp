import imp
import py_compile
from django.urls import URLPattern, path
from pip import main
from .views import chart_select_view, add_purchase_view, sales_dist_view


app_name = 'products'

urlpatterns = [
    path('', chart_select_view, name='main-products-view'),
    path('add/', add_purchase_view, name='add-purchase-view'),
    path('sales/', sales_dist_view, name='sales-view')
]


