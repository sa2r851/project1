from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter


# manager and admin
class DeliveryListView(generics.ListAPIView):
    queryset = DeliveryProfile.objects.all()
    serializer_class = DeliverySerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['country','city']
    search_fields = ['user']
# manager and admin and delivery
class StoreListView(generics.ListAPIView):
    queryset = StoreProfile.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['country','city']
    search_fields = ['user']

# only admin
class ManagerListView(generics.ListAPIView):
    queryset = Area_ManagerProfile.objects.all()
    serializer_class = ManagerSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['country']
    search_fields = ['user']
# manager and admin and delivery
class PharmaListView(generics.ListAPIView):
    queryset = PharmacistProfile.objects.all()
    serializer_class = PharmacySerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['country','city']
    search_fields = ['user']