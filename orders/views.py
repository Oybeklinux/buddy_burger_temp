from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None


class FilialViewSet(viewsets.ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
