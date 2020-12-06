from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Note
from .serializers import NoteSerailizer
from rest_framework.exceptions import PermissionDenied


# Create your views here.

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class NoteViewSet(viewsets.ModelViewSet):
    # queryset = Note.objects.all()
    serializer_class = NoteSerailizer
    permission_classes = (IsOwner, )

    # Ensure a user sees only own Note objects
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Note.objects.filter(owner=user)
        raise PermissionDenied()

    #set user as owner of a Notes object
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


