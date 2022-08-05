from rest_framework import serializers

from .models import *


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'


class FilialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filial
        fields = '__all__'