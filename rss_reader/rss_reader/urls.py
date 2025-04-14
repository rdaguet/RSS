from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Access to Django administration interface
    path('admin/', admin.site.urls),
    # Inclusion of “feeds” application routes under the /api/ prefix
    path('api/', include('feeds.urls')),
]
