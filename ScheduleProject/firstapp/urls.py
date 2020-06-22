from django.urls import path
from firstapp import views

app_name = 'firstapp'


urlpatterns = [
    path('mainpage/', views.schedulepage, name='schedule_page'),
    path('mainpage/input/', views.topic, name='topic'),
    path('schedule/', views.schedule, name='design_schedule'),
    path('schedule/data1', views.empData, name='emp_date_data'),
    path('schedule/data_schedule_prev', views.emp_schedule, name='emp_schedule_data'),
    path('schedule/add_data', views.emp_save_data, name='save_schedule_data'),
    path('schedule/delete_schedule', views.delete_schedule, name='delete_schedule_data'),
]
