from django.shortcuts import render
from .serializers import UserSerializer, InformationSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Information
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InformationList(generics.ListCreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ('id', 'name', 'age')
    ordering_fields = ('cr_time')


class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('users', request=request, format=format),
            'informations': reverse('informations', request=request, format=format),
        })
