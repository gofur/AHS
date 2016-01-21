from django.db import models
from django.contrib.auth.models import User

if not hasattr(User, 'mobilephone'):
    field = models.CharField(max_length=12, blank=True)
    field.contribute_to_class(User, 'mobilephone')

if not hasattr(User, 'alamat'):
    field = models.TextField(max_length=500, blank=True)
    field.contribute_to_class(User, 'alamat')
