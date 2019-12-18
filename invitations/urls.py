from django.urls import path
from invitations.views import InvitationsList, InvitationDetail

urlpatterns = [
    path('invitations/', InvitationsList.as_view()),
    path('invitations/<str:id>/', InvitationDetail.as_view()),
]
