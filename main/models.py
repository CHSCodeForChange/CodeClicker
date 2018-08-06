from django.db import models


class Code(models.Model):
    objects = models.Manager()
    clicks = models.IntegerField(null=False, blank=False, default=0)
    prize = models.IntegerField(null=False, blank=False, default=0)


class User(models.Model):
    ip = models.GenericIPAddressField(null=False)
    name = models.CharField(max_length=240, null=False, blank=False, default="Anonymous")
    clicks = models.IntegerField(null=True, blank=False, default=0)