from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import MyTokenObtainPairView

urlpatterns = [
    path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
