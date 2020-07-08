from django.shortcuts import render

from samba import (
    models,
    permissions,
    serializers,
)

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email',]
    ordering_fields = ['first_name', 'last_name', 'email']

