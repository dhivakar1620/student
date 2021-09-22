from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/student', views.student, name='student'),
    path('api/student/results', views.result,name='result'),
    path('api/student/<ass>/mark', views.mark, name='mark'),
    path('api/student/<ass>/mark/add', views.add, name='add'),
    path('api/student/search', views.search, name='search'),
    path('api/student/<ass>/delete', views.delete, name='del'),
]


#(?<i_id>\d+)    (?P<pk>[0-9]+)   <int:pk>
