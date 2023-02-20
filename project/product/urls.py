from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import api
from rest_framework_nested import routers

router=DefaultRouter()
router.register('offers',api.OfferView)
router.register('manage',api.IdleView)
router.register('cart',api.CartViewset)
#router.register('ckeckout',api.ckeckout,basename='checkout')
#router.register('ret',api.RetrieveCart)
#router.register('del',api.DestroyCart)

cart_router=routers.NestedDefaultRouter(router,'cart',lookup="cart")
cart_router.register("items",api.CartItemViewSet,basename="cart_items")
urlpatterns = [

    path("",include(router.urls)),
    path("",include(cart_router.urls)),

    path("companies",api.CompanyListView.as_view(),name='Companies'),
    #path("idle",api.IdleView.as_view(),name='idle'),# 2
    #path('checkout/', api.ckeckout.as_view()),

    path("companies/products",api.products_campany,name='products of company'),
    path("checkout/<str:pk>",api.confirm_order,name='checkout'),


]
