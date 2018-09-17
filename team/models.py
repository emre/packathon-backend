from django.db import models
from project.models import Project

from common.models import Hacker


class Team(models.Model):
    """
    Model for Teams
    """
    name = models.CharField(max_length=255, blank=False, null=False)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, blank=True, null=True)
    founder = models.ForeignKey(Hacker, related_name="founder")
    members = models.ManyToManyField(Hacker, blank=True, null=True, related_name="members")

    def __str__(self):
        return self.name
