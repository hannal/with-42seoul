from django.contrib import admin
from django.urls import path

from accounts import views as accounts_views


urlpatterns = [
    path('signup/', accounts_views.signup),
    path('admin/', admin.site.urls),
]
