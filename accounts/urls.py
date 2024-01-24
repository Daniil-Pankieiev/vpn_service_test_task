from django.urls import path

from accounts.views import (
    UserDetailView,
    UserUpdateView,
    LogoutConfirmation,
    UserRegisterView,
)


urlpatterns = [
    path("profile/", UserDetailView.as_view(), name="profile"),
    path("profile/update/", UserUpdateView.as_view(), name="update_profile"),
    path("accounts/register/", UserRegisterView.as_view(), name="register"),
    path(
        "accounts/confirm-logout/",
        LogoutConfirmation.as_view(),
        name="confirm_logout",
    ),
]

app_name = "account"
