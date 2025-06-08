
from django.urls import path, include

urlpatterns = [
    path('', include('charts.urls')),
]
