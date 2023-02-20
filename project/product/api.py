from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics ,viewsets
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerPharmacy , IsOwnerStore
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.mixins import CreateModelMixin , RetrieveModelMixin ,DestroyModelMixin
from rest_framework.viewsets import GenericViewSet ,ModelViewSet
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework.views import APIView

from rest_framework.pagination import PageNumberPagination
#
class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['name']
    authentication_classes = [TokenAuthentication]
    pagination_class=PageNumberPagination
    # permission_classes = [IsAuthenticated]

# منتجات الشركة
@api_view(['GET'])
def products_campany(request):
    details=Item.objects.filter(Company=Company.company_id)
    data=ItemSerializer(details,many=True).data
    return Response({'data':data})
# قائمة الاقسام الرئيسية
@api_view(['GET'])
def products_campany(request):
    details=Offer.objects.filter(Company=Company.company_id)
    data=OfferSerializer(details,many=True).data
    return Response({'data':data})
# pharmacy and store
class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['name','slug','effective_material']
    filterset_fields = ['shape','letter','company']
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
#only owner Pharmacy
class IdleView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = IdleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerPharmacy]
# pharmacy
class IdleListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = IdleSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['name','slug','effective_material']
    filterset_fields = ['shape','letter','company']
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
# pharmacy
class OfferListView(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['product.name','product.slug','product.effective_material']
    filterset_fields = ['prodect.shape','prodect.letter','prodect.company','prodect.section']
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

#only stores
class OfferView(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = ItemOfferSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerStore]


class CartViewset(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class RetrieveCart(RetrieveModelMixin,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DestroyCart(DestroyModelMixin,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    http_method_names=['get','post','delete','patch']
    def get_queryset(self):
        return Cartitems.objects.filter(cart_id=self.kwargs["cart_pk"])
    def get_serializer_class(self):
        if self.request.method=="POST":
            return AddCartItemSerializer
        elif self.request.method=="PATCH":
            return UpdateCartitemSerializer
        return CartitemSerializer
    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes([IsAuthenticated],)
def confirm_order(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.completed = True
    cart.save()
    messages.success(request, "تم ارسال طلبك")
    Cart.objects.create(Pharmacy=request.user)
    return HttpResponseRedirect(redirect_to='https://google.com')


class ckeckout(APIView):
    serializer_class=CartSerializer
    def post(request, pk):
        user =request.user
        cart = Cart.objects.get(id=pk,Pharmacy=user,completed=False)
        cart.completed = True
        cart.save()
        messages.success(request, "تم ارسال طلبك")
        Cart.objects.create(Pharmacy=request.user)
        return HttpResponseRedirect(redirect_to='https://google.com')




class OrderListView(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(Pharmacy=user,completed=True,is_received=False)
    serializer_class = CartSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerPharmacy]

@api_view(['GET'])
def in_progress_orders(request):
    details=Cart.objects.filter(Pharmacy=request.user,completed=True,is_received=False)
    data=CartSerializer(details,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def previous_orders(request):
    details=Cart.objects.filter(Pharmacy=request.user,completed=True,is_received=True)
    data=CartSerializer(details,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def all_in_progress_orders(request):
    details=Cart.objects.filter(completed=True,is_received=True)
    data=CartSerializer(details,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def all_previous_orders(request):
    details=Cart.objects.filter(completed=True,is_received=True)
    data=CartSerializer(details,many=True).data
    return Response({'data':data})