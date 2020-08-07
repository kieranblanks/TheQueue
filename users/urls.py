from django.contrib import admin
from django.urls import path
from users import home, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    # path('signup/', signup_view, name "signup")
]