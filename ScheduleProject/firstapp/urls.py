from django.urls import path
from firstapp import views

app_name = 'firstapp'


urlpatterns = [
    path('mainpage/', views.schedulepage, name='schedule_page'),
    path('mainpage/input/', views.topic, name='topic'),
    path('schedule/', views.schedule, name='design_schedule'),
    path('schedule/data1', views.empData, name = 'emp_date_data'),
]
