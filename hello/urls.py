from django.urls import path
from .views import hello_view

app_name = 'hello'

urlpatterns = [
    # path("", views.home, name="home"),
    path("<name>", hello_view, name="hello-view")
]
