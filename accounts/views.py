from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.account.models import EmailAddress
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.registration.serializers import (ResendEmailVerificationSerializer)


def verify_email(request, key):
    return redirect(f"http://localhost:3000/registration/verify-email/{key}")

def password_reset_confirm(request, uid, token):
    return redirect(f"http://localhost:3000/password/reset/confirm/{uid}/{token}")

class ResendEmailVerificationView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ResendEmailVerificationSerializer
    queryset = EmailAddress.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print ("Data on resend:", request.data)
        serializer.is_valid(raise_exception=True)

        email = self.get_queryset().filter(**serializer.validated_data).first()
        if email and not email.verified:
            email.send_confirmation(request)
            return Response({'detail': _('ok')}, status=status.HTTP_200_OK)
        elif email and email.verified: 
            print ("Email address already verified.")
            return Response({'detail': _('Email address already verified.')}, status=status.HTTP_204_NO_CONTENT)
        elif email is None : 
            print ("Email address does not exist.")
            return Response({'detail': _('Email address does not exist.')}, 
            status=status.HTTP_404_NOT_FOUND)


# class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = "http://localhost:3000/"
#     client_class = OAuth2Client
