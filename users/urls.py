from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("user-authorisation/<slug:phoneNumber>", views.userAuthorisation),
    path("code-enter/<slug:phoneNumber>/<slug:code>", views.codeEnter),
    path("user/<slug:phoneNumber>", views.usersRequest),
    path("invite-code-insert/<slug:phoneNumber>/<slug:inviteCode>", views.inviteCodeInsert),
    path("users-invite-code-filled/", views.usersInviteCodeFilled),
]