from django.contrib import admin
from leads.models import Lead


class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'created_at')

admin.site.register(Lead, LeadAdmin)
