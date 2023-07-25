from django.urls import path
from prj_1.views import index,addnew,savenew

urlpatterns = [
   path('', index),
   path('new/', addnew),
   path('save/', savenew),
]