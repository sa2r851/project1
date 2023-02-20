from django.contrib import admin
from django.urls import path , include
from . import api
from .views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView

app_name='storeapp'
urlpatterns = [
    path("pharm/",api.PharmaListView.as_view(),name='Pharmacies List'),
    path("manager/",api.ManagerListView.as_view(),name='Manager List'),
    path("store/",api.StoreListView.as_view(),name='Stores List'),
    path("delivery/",api.DeliveryListView.as_view(),name='Delivery List'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
