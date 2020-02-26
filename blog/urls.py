from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]