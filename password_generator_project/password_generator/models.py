#models.py
from django.db import models

# Create your models here.
# In password_generator/models.py

from django.db import models

class GeneratedPassword(models.Model):
    password = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.password
