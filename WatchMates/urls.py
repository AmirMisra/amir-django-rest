from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('wla/', include('WatchList_app.api.urls')),
    path('account/', include('user_app.api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
]
