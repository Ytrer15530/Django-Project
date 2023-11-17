from django.shortcuts import render
from rest_framework import viewsets
from .models import Payments
from .serializers import PaymentsSerializer


class PaymentViews(viewsets.ModelViewSet):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.order_by('id')
