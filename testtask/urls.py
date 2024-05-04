from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path("", include("users.urls")),
    path("user-authorisation/<slug:phoneNumber>", include("users.urls")),
    path("code-enter/<slug:phoneNumber>/<slug:code>", include("users.urls")),
    path("user/<slug:phoneNumber>", include("users.urls")),
    path("invite-code-insert/<slug:phoneNumber>/<slug:inviteCode>", include("users.urls")),
    path("users-invite-code-filled/", include("users.urls")),
]