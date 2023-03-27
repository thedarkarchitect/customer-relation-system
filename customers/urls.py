from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete/<int:pk>', views.delete_record, name='delete'),
    path('add_record', views.add_record, name='add'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
]
