from django.http import JsonResponse
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import serializers as rest_serializers
from rest_framework.views import APIView
from .serializer import UserListRetrieveSerializer,UserCreateUpdateSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListRetrieveSerializer
        elif self.request.method == 'POST':
            return UserCreateUpdateSerializer

class UserRetrieveUpdateAPIViewAPIView(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    lookup_field='username'

    def perform_update(self, serializer):
        """Check if the loggedin user is the creator of the user"""
        if self.request.user.username == serializer.instance.username:
            super().perform_update(serializer)
        else:
            raise rest_serializers.ValidationError('This user is not you')


    def get_serializer_class(self,*args, **kwargs):
        if self.request.method == 'GET':
            return UserListRetrieveSerializer

        elif self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UserCreateUpdateSerializer

        else:
            return super().get_serializer(*args, **kwargs)



class ChangePassword(APIView):
    queryset = get_user_model().objects.none()
    def post(self,request):
        user=request.user
        try:
            old_password = request.data['old_password']
            new_password = request.data['new_password']
        except:
            return JsonResponse({'message':"Invalid parameters"},status=500)
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return JsonResponse({'message':"Password Changed"}, status=200)
        else:
            return JsonResponse({'message':"Old password is not valid"}, status=500)