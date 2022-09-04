from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from account.views import (
    RegitsterView,
    ForgetPasswordView,
    # LogoutView,
)

urlpatterns = [
    path('register/', RegitsterView.as_view(), name='RegitsterView'),
    # path('logout/', LogoutView.as_view(), name='RegitsterView'),
    path('forgotpassword/', ForgetPasswordView.as_view(), name='RegitsterView'),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]
