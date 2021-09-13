from django.urls import path, include
from .api.views import NoteListCreateAPIView, NoteRetrieveUpdateAPIViewAPIView, GetShareNoteSharedByAPIView, \
    GetShareNoteWithMeAPIView,CreateSharNoteAPIView

urlpatterns = [
    path('api/v1/', NoteListCreateAPIView.as_view()),
    path('api/v1/<str:unique_id>/', NoteRetrieveUpdateAPIViewAPIView.as_view()),
    path('shared/api/v1/', GetShareNoteSharedByAPIView.as_view()),
    path('sharedwith/api/v1/', GetShareNoteWithMeAPIView.as_view()),
    path('share/api/v1/', CreateSharNoteAPIView.as_view()),
]
