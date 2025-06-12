from django.urls import path
from . import views




urlpatterns=[
    path('members/',views.members,name='members'),
    path('members/register/',views.register,name='register'),
    path('members/register/registerdb/',views.registerdb,name='registerdb'),
    path('members/login/',views.login,name='login'),
    path('members/login/logindb/',views.logindb,name='logindb'),
    path('record',views.record,name='record'),
    path('login',views.registerdb,name='registerdb'),
    path('record/', views.record, name='record'),

]


