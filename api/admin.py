from django.contrib import admin
from .models import *
import csv
from django.http import HttpResponse
# Register your models here.

admin.site.register(Subscriber)
admin.site.register(Destination)
# admin.site.register(TravelInquiry)

@admin.register(TravelInquiry)
class TravelInquiryAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone",
        "preferred_destination",
        "travel_date",
        "created_at",
    )
    list_filter = ("preferred_destination", "travel_date", "created_at")
    search_fields = ("full_name", "email", "phone", "message")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [
            "full_name",
            "email",
            "phone",
            "preferred_destination",
            "travel_date",
            "message",
            "created_at",
        ]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename={meta.verbose_name_plural}.csv"
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = []
            for field in field_names:
                value = getattr(obj, field)
                if field == "preferred_destination" and value is not None:
                    value = str(value)
                row.append(value)
            writer.writerow(row)

        return response

    export_as_csv.short_description = "Export selected inquiries to CSV"