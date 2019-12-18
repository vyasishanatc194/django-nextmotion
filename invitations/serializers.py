import datetime
from rest_framework import serializers
from invitations.models import Invitation
from django.contrib.auth.models import User
from django.utils.timezone import utc

class InvitationSerializer(serializers.ModelSerializer):
    creatorEmail = serializers.SerializerMethodField('get_creator_email')
    creatorFullname = serializers.SerializerMethodField('get_creator_full_name')
    seconds = serializers.SerializerMethodField('get_seconds')
    class Meta:
        model = Invitation
        fields = ["id", "created_time", "seconds", "email", "used", "creatorEmail", "creatorFullname", "creator"]
        read_only_fields = ['id']
        extra_kwargs = {
            "creator": {"write_only": True}
        }
    
    def get_seconds(self, obj):
        # The time since the invitation has been created in seconds
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        timediff = now - obj.created_time
        return int(timediff.total_seconds())
    
    def get_creator_email(self, obj):
        if obj.creator:
            return obj.creator.email
    
    def get_creator_full_name(self, obj):
        if obj.creator:
            return "{} {}".format(obj.creator.first_name, obj.creator.last_name).strip()

class InvitationPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ["id", "email", "used"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "email": {"write_only": True},
            "used": {"write_only": True}
        }
