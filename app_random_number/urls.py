from _settings import urls
from django.urls import path
from app_random_number.views import Number

urlpatterns = [
    path('', Number.as_view())
]