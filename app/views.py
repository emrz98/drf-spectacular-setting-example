from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class Player(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data_example = {"reponse": "myresponse"}
        return Response(data_example)