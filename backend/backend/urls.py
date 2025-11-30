from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # API routes from dashboard_app
    path('api/', include('dashboard_app.urls')),
]
