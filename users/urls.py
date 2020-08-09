from django.contrib import admin
from django.urls import path
from users import home, signup_view
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('users/', views.register, name='Signup'),
    # path('signup/', signup_view, name "signup")
]