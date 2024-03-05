from django.urls import path
from . import views

urlpatterns = [
    path('',views.calculator,name="calculator"),
    path('submitquery',views.submitquery,name='submitquery'),
]
