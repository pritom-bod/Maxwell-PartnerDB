from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from .models import Partner
from .serializers import PartnerSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # HQ অনুযায়ী ফিল্টার
    filterset_fields = ["hq"]
    # সব ফিল্ডে সার্চ
    search_fields = [
        "firm_name", "hq", "focus_area",
        "contact", "donor_experience", "current_partnership_status"
    ]

class PartnerPagination(PageNumberPagination):
    page_size = 10               # ডিফল্ট আইটেম সংখ্যা প্রতি পেজে
    page_size_query_param = 'page_size'  # ইউজার চাইলে page size change করতে পারবে
    max_page_size = 100     

@api_view(["GET"])
@permission_classes([AllowAny])
def hq_list(request):
    hqs = Partner.objects.exclude(hq__isnull=True).exclude(hq__exact="").values_list("hq", flat=True).distinct()
    return Response(sorted(hqs))
