from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('anc/', views.students_list, name='students_list'),
    path('anc/update/<int:id>', views.update, name='update'),
    path('anc/delete/<int:id>', views.delete, name='delete'),
    path('anc/create/', views.create, name='insert'),
    path('anc/login/', views.login, name='login'),
    path('anc/testlogin/', views.testlogin, name='testlogin'),
    path('anc/signup/', views.signup, name='signup'),
    

]