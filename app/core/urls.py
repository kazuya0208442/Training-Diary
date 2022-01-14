from django.urls import path, include
from .views import Target_detail, TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate, Home, Card_detail


urlpatterns = [
    path('list', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
    
    path('', Home.as_view(), name='home'),
    path('t_detail/<int:pk>', Target_detail.as_view(), name='t_detail'),
    path('c_detail/<int:pk>', Card_detail.as_view(), name='c_detail'),
]
