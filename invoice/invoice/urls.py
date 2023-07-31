from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from invoiceapp.views import InvoiceViewSet, InvoiceDetailViewSet

# Create the viewsets
invoice_viewset = InvoiceViewSet.as_view({'get': 'list', 'post': 'create'})
invoice_detail_viewset = InvoiceDetailViewSet.as_view({'get': 'list', 'post': 'create'})

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoices/', invoice_viewset, name='invoice-list'),
    path('invoice-details/', invoice_detail_viewset, name='invoice-detail-list'),
]

# Optional: Add format_suffix_patterns if you want to support response format suffixes like '.json' or '.api'.
# This is useful for clients that want to specify the desired response format in the URL.
urlpatterns = format_suffix_patterns(urlpatterns)
