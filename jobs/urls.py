from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),

    path('job/<int:job_id>/', views.job_detail),

    path('favorite/<int:job_id>/', views.toggle_favorite),

    path('favorites/', views.favorites),

    path('login/', views.login_view),

    path('logout/', views.logout_view),

    path('register/', views.register_view),

]