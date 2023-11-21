from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('spec1/',spec1,name='spec1'),
    path('spec2/',spec2,name='spec2')
]