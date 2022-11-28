from django.urls import path
from .import views
app_name='commen'

urlpatterns = [
    path('',views.home,name='index'),
    path('school',views.school,name='school_login'),
    path('teacher',views.teacher,name='teacher_login'),
    path('student',views.student,name='student_login'),
    path('sumathi',views.sumathi,name='sumathi'),
    path('css',views.css,name='css'),
    path('css1',views.css1,name='css1')




]


