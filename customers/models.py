# Django model file to create Customer objects in db
from django.db import models


class Customer(models.Model):
    

    # username = db.Column(db.String(50), unique=True, nullable=False)
    # password = db.Column(db.String(50), nullable=False)
    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    aadhaar_number = models.CharField(max_length=12)
    assigned_mobile_number = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_related_name = 'customers'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
        ordering = ['id']

    def __str__(self):
        return self.name
