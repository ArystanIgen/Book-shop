from django.shortcuts import render
from .models import *
from rest_framework import generics, mixins, viewsets
from .serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    # queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    def list(self, request):
        serializer = BookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

class JournalViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    # queryset = Book.objects.all()
    serializer_class = JournalSerializer

    def get_queryset(self):
        return Journal.objects.all()

    def list(self, request):
        serializer = JournalSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)