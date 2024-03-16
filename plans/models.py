# Django model file to create Plan objects in db

from django.db import models


PLAN_CHOICES = {
    "platitnum365": "Platinum365",
    "gold180": "Gold180",
    "silver90": "Silver90"
}

PLAN_COST_CHOICES = {
    "499": 499,
    "299": 299,
    "199": 199
}

VALIDITY_CHOICES = {
    "365_days": 365,
    "180_days": 180,
    "90_days": 90
}

class Plan(models.Model):
    name = models.CharField(PLAN_CHOICES, default="silver90", max_length=20)
    cost = models.IntegerField(PLAN_COST_CHOICES, default="199", max_length=10)
    validity = models.IntegerField(VALIDITY_CHOICES, default="90_days", max_length=10)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_related_name = 'plans'
        verbose_name = 'plan'
        verbose_name_plural = 'plans'
        ordering = ['id']

    def __str__(self):
        return self.name
