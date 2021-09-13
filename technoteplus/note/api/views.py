from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import serializers as rest_serializers
from rest_framework.views import APIView

from .serializer import NoteCreateUpdateSerializer, NoteListRetrieveSerializer, SharedNoteSerializer
from ..models import Note, SharedNote


class NoteListCreateAPIView(generics.ListCreateAPIView):

    def get_queryset(self):
        return Note.objects.filter(created_by=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return NoteListRetrieveSerializer
        elif self.request.method == 'POST':
            return NoteCreateUpdateSerializer


class NoteRetrieveUpdateAPIViewAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    lookup_field = 'unique_id'

    def perform_destroy(self, instance):
        if self.request.user.username == instance.created_by.username:
            super().perform_destroy(instance)
        else:
            raise rest_serializers.ValidationError('This note was not created to you')

    def perform_update(self, serializer):
        """Check if the loggedin user is the creator of the user"""
        if self.request.user.username == serializer.instance.created_by.username:
            super().perform_update(serializer)
        else:
            raise rest_serializers.ValidationError('This note was not created to you')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return NoteListRetrieveSerializer
        elif self.request.method == 'PUT' or self.request.method == 'PATCH':
            return NoteCreateUpdateSerializer

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class GetShareNoteSharedByAPIView(APIView):
    queryset = SharedNote.objects.none()

    def get(self, request):
        data = SharedNote.objects.filter(created_by=request.user)
        serializer = SharedNoteSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


class GetShareNoteWithMeAPIView(APIView):
    queryset = SharedNote.objects.none()

    def get(self, request):
        data = SharedNote.objects.filter(shared_with=request.user)
        serializer = SharedNoteSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


class CreateSharNoteAPIView(APIView):
    queryset = SharedNote.objects.none()

    def post(self, request):
        for shared in request.data['share_with']:
            try:
                shared_with = get_user_model().objects.get(id=shared)
                note = Note.objects.get(id=request.data['note'])
            except:
                data = {'status': 'error','message':'Invalid Parameters'}
                return JsonResponse(data, safe=False)
            if len(SharedNote.objects.filter(shared_with=shared_with, note=note)) == 0:
                SharedNote.objects.create(shared_with=shared_with, note=note, created_by=request.user,
                                          updated_by=request.user)
        data = {'status': 'success','message':'Successfully Shared'}
        return JsonResponse(data, safe=False)
