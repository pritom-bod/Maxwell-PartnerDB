from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from .models import Partner
from .serializers import PartnerSerializer

# Custom Pagination Class
class PartnerPagination(PageNumberPagination):
    page_size = 5                
    page_size_query_param = "page_size"  
    max_page_size = 100

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all().order_by("id")
    serializer_class = PartnerSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["hq"]
    search_fields = [
        "firm_name", "hq", "focus_area",
        "contact", "donor_experience", "current_partnership_status"
    ]
    pagination_class = PartnerPagination   # pagination add

@api_view(["GET"])
@permission_classes([AllowAny])
def hq_list(request):
    hqs = Partner.objects.exclude(hq__isnull=True).exclude(hq__exact="").values_list("hq", flat=True).distinct()
    return Response(sorted(hqs))
