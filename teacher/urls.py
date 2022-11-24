from django.urls import path
from .import views
app_name='teacher'
urlpatterns = [
    path('home',views.home,name='index'),
    path('attendance',views.attendance,name='attendance'),
    path('profile',views.profile,name='profile'),
    path('viewstudents',views.viewstudents,name='studentview')

]


