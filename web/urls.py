from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tools/distance/', views.smart_tools_distance, name='tool_distance'),
    path('tools/cost/', views.smart_tools_cost, name='tool_cost'),
    path('tools/currency/', views.smart_tools_currency, name='tool_currency'),
]
