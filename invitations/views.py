from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from invitations.models import Invitation
from invitations.serializers import InvitationSerializer, InvitationPatchSerializer

from invitations.utils import send_email

# Pagination Configuration
paginator = PageNumberPagination()
paginator.page_size = 5

# Create your views here.

class InvitationsList(APIView):
    """
    List all Invitations, or create a new Invitation.
    """
    def get(self, request, format=None):
        invitations = Invitation.objects.all().order_by('-created_time')
        invitations = paginator.paginate_queryset(invitations, request)
        serializer = InvitationSerializer(invitations, many=True)
        return Response({
            'links': {
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link()
            },
            'count': paginator.page.paginator.count,
            'data': serializer.data
        })

    def post(self, request, format=None):
        if "creator" not in request.data.keys():
            request.data["creator"] = User.objects.first().id
        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_email(serializer.data['email']) # Send Email
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvitationDetail(APIView):
    """
    Retrieve, update or delete a Invitation instance.
    """
    def get_object(self, id):
        try:
            return Invitation.objects.get(id=id)
        except Invitation.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        invitation = self.get_object(id)
        serializer = InvitationSerializer(invitation)
        return Response(serializer.data)

    def patch(self, request, id, format=None):
        invitation = self.get_object(id)
        exist_email = invitation.email
        serializer = InvitationPatchSerializer(invitation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if exist_email != request.data['email']:
                send_email(request.data['email'])
                data = {}
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        invitation = self.get_object(id)
        invitation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
