
from django.db import models
from datetime import datetime

# Create your models here.
class Invoice(models.Model):
    date = models.DateField("Date", default=datetime.now)
    invoice_no = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    unit_price = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.quantity
