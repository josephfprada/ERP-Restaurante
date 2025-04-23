
from django.contrib import admin
from django.urls import path
from account.views import user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login')
]
