

from django.contrib import admin
from .models import Partner

# Register your models here.

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("firm_name", "hq", "focus_area", "contact", "donor_experience", "current_partnership_status")
    search_fields = ("firm_name", "hq", "focus_area", "contact", "donor_experience", "current_partnership_status")
    list_filter = ("hq",)
