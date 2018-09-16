from rest_framework import viewsets
from django.http import JsonResponse, Http404
from django.contrib.auth import get_user_model
from common.serializers import HackerSerializer


class HackerViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = HackerSerializer
    filter_fields = ('first_name', 'team')