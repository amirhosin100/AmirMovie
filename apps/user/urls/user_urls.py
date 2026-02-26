from django.urls import path

from apps.user.views.user_views import (
    UserRegistrationView,
    UserInfoView
)

app_name = 'normal_user'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('info/', UserInfoView.as_view(), name='info'),
]
