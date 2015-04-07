from django.db import models

class group(models.Model):
    groups = models.CharField(max_length=1000, blank=True)
    className = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.className
