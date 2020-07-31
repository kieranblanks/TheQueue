from django.contrib import admin
from django.urls import path
from accounts.views import home_view, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    # path('signup/', signup_view, name "signup")
]