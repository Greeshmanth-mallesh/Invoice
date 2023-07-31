from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['date', 'invoice_no', 'customer_name']

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['invoice', 'description', 'quantity', 'unit_price', 'price']
