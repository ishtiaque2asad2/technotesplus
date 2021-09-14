from django.urls import path, include
from .api.views import NoteListCreateAPIView, NoteRetrieveUpdateAPIViewAPIView, GetShareNoteSharedByAPIView, \
    GetShareNoteWithMeAPIView,CreateSharNoteAPIView,DetailSharedNoteWithAPIView,DetailSharedNoteByAPIView

urlpatterns = [
    path('sharedwithme/api/v1/<str:unique_id>/', DetailSharedNoteWithAPIView.as_view()),
    path('sharedbyme/api/v1/<str:unique_id>/', DetailSharedNoteByAPIView.as_view()),
    path('api/v1/<str:unique_id>/', NoteRetrieveUpdateAPIViewAPIView.as_view()),

    path('api/v1/', NoteListCreateAPIView.as_view()),
    path('share/api/v1/', CreateSharNoteAPIView.as_view()),
    path('sharedbyme/api/v1/', GetShareNoteSharedByAPIView.as_view()),
    path('sharedwithme/api/v1/', GetShareNoteWithMeAPIView.as_view()),


]
