from django.urls import path,include
from .api.views import UserListCreateAPIView,UserRetrieveUpdateAPIViewAPIView

urlpatterns = [
    path('api/v1/', UserListCreateAPIView.as_view()),
    path('api/v1/<str:username>/', UserRetrieveUpdateAPIViewAPIView.as_view()),

]
