from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from project.models import Project
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination


class Hacker(AbstractUser):
    """
    Custom User object with more details
    """
    name = models.CharField(max_length=255)
    profile_about = models.CharField(max_length=255, blank=True, null=True)
    profile_location = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username


class AuthenticationMethod(SessionAuthentication):
    """
    Ignore CSRF for enabling Token access to api
    """
    def enforce_csrf(self, request):
        # Do not check csrf to be able to login both over web and api
        return


class ApiPagination(PageNumberPagination):
    """
    Pagination params for list results in api
    """
    page_size = 100
    page_size_query_param = 'page_size'
