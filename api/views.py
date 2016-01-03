from . import serializers
from django.http import QueryDict
from orders.models import Order
from rest_framework import generics, status, viewsets, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
import copy
import logging
import orders


logger = logging.getLogger(__name__)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()

    @list_route(methods=['POST'], permission_classes=[permissions.AllowAny])
    def postback(self, request):
        logger.debug('{} {}'.format(request.get_full_path(), request.body))

        try:
            order_id = int(request.data.get('order_id', 0))
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        partial = True
        try:
            instance = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            instance, partial = None, False

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save(data=request.data)

        return Response(serializer.data)
