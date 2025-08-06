from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', views.index, name='index'),

]
