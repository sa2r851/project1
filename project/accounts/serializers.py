from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from djoser.serializers import UserCreateSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields =fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields =fields = "__all__"

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreProfile
        fields =fields = "__all__"

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacistProfile
        fields =fields = "__all__"

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryProfile
        fields =fields = "__all_"

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area_ManagerProfile
        fields =fields = "__all_"

class Mycreate(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields=['username','password','id','role']