from django.urls import path, include
from .views import CardUpdate, Staff_detail, StaffUpdate, Target_detail, Home, Card_detail, Test, Week_detail, WeekUpdate, TargetUpdate


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('t_detail/<int:pk>', Target_detail.as_view(), name='t_detail'),
    path('c_detail/<int:pk>', Card_detail.as_view(), name='c_detail'),
    path('w_detail/<int:pk>', Week_detail.as_view(), name='w_detail'),
    path('s_detail/<int:pk>', Staff_detail.as_view(), name='s_detail'),
    path('t_update/<int:pk>', TargetUpdate.as_view(), name='t_update'),
    path('c_update/<int:pk>', CardUpdate.as_view(), name='c_update'),
    path('s_update/<int:pk>', StaffUpdate.as_view(), name='s_update'),
    path('w_update/<int:pk>', WeekUpdate.as_view(), name='w_update'),
    path('test', Test.as_view(), name='test'),
]
