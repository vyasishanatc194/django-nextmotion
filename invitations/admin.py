from django.contrib import admin
from invitations.models import Invitation
# Register your models here.

class InvitationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Invitation, InvitationAdmin)
