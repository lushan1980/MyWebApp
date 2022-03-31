from django.urls import URLPattern, path
from pip import main
from .views import upload_file_view


app_name = 'drug'

urlpatterns = [
    path('upload/', upload_file_view, name='upload-view'),
]
