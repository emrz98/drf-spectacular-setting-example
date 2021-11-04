from drf_spectacular.generators import SchemaGenerator
from drf_spectacular.hooks import preprocess_exclude_path_format
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework.authentication import BasicAuthentication


class CustomSchema(SchemaGenerator):
    def __init__(self):
        self.endpoints = None
        print(self.urlconf)


def custome_preprocessing(endpoints):
    print(endpoints)
    print(endpoints[0:2])
    return endpoints[0:3]


@permission_classes((IsAuthenticated, ))
@authentication_classes([BasicAuthentication])
def custome_postprocessing(result, generator, request, public):
    ip = request.META.get('REMOTE_ADDR')
    print(public)
    print(ip)
    print(request)
    print(request.user)
    print(generator)
    return result


class CustomSpectacularSwaggerView(SpectacularSwaggerView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated, )