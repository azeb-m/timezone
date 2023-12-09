from django.urls import path
from .views import showt

urlpatterns = [
    path('', showt, name='ethiopia'),
]
