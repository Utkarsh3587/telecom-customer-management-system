# Django model file to create Subscriber objects in db
# Subscriber is the customer who gets enrolled in a plan.
from django.db import models


class Subscriber(models.Model):
    

    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    plan =  models.ForeignKey('plans.Plan', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    class Meta:
        default_related_name = 'subscribers'
        verbose_name = 'subscriber'
        verbose_name_plural = 'subscribers'
        ordering = ['id']

    def __str__(self):
        return self.id
