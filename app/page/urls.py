
from django.urls import path, include
from .views import *

urlpatterns = [
    path('page-list', PageListView.as_view(), name='page-list'),
    path('page-detail/<int:pk>', PageDetail.as_view(), name='page-detail'),
]