from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Utilizador(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    tipo = models.IntegerField(default = 2)

    def __unicode__(self):
        return self.user.username
 