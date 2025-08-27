from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),   # ✅ Products API
    path('api/', include('users.urls')),      # ✅ Users API (will create later)
]
