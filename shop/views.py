from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .models import Item, Category, Order
from .serializers import ItemSerializer, CategorySerializer, OrderSerializer
from .permissions import IsAuthorPermission, IsSenderPermission, IsBuyerPermission
from .paginations import StandartPagination


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication,  ]
    permission_classes = [IsAuthorPermission, IsSenderPermission, ]
    pagination_class = StandartPagination


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, IsSenderPermission ]

    def get_queryset(self):
        return self.queryset.filter(category_id=self.kwargs['category_id'])

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            item=get_object_or_404(Category, id=self.kwargs['category_id'])
        )

class ItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, IsSenderPermission]



class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, IsBuyerPermission,]

    def get_queryset(self):
        return self.queryset.filter(item_id=self.kwargs['item_id'])

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            item=get_object_or_404(Category, id=self.kwargs['item_id'])
        )

class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, IsBuyerPermission, ]






