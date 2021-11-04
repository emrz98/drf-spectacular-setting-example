from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from drf_spectacular.generators import SchemaGenerator
class Player(APIView):
    #authentication_classes = (BasicAuthentication,)
    #permission_classes = (IsAuthenticated,)
    @extend_schema()
    def get(self, request):
        data_example = {"reponse": "myresponse"}
        return Response(data_example)


class AnotherPlayer(APIView):
    @extend_schema()
    def get(self, request):
        data_example = {"reponse": "myresponse"}
        return Response(data_example)