from django.contrib import admin
from django.urls import path, include
from reviews.views import (
    UserCreateView,
    AdminUserCreateView,
    CustomTokenObtainPairView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', UserCreateView.as_view(), name='user-register'),
    path('api/auth/register/admin/', AdminUserCreateView.as_view(), name='admin-register'),
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('api/', include('reviews.urls')),
]