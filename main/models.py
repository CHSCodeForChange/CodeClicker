from django.db import models


class Code(models.Model):
    objects = models.Manager()
    clicks = models.IntegerField(null=False, blank=False, default=0)
    prize = models.IntegerField(null=False, blank=False, default=0)
