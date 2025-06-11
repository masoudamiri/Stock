
from django.urls import path
from .views import chart_view, about_view, market_view

urlpatterns = [
    path('', chart_view, name='chart'),
    path('market/', market_view, name='market'),
    path('about/', about_view, name='about'),
]
