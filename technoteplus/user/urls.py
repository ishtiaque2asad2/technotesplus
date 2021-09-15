from django.urls import path,include
from .api.views import UserListCreateAPIView, UserRetrieveUpdateAPIViewAPIView, ChangePassword

urlpatterns = [
    path('api/v1/changepassword/', ChangePassword.as_view()),
    path('api/v1/<str:username>/', UserRetrieveUpdateAPIViewAPIView.as_view()),
    path('api/v1/', UserListCreateAPIView.as_view()),




]
