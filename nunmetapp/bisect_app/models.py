from django.db import models
from django.contrib.auth.models import User

class BisectOutput(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank=True)
    f_s=models.CharField(max_length=200, null=False)
    root=models.FloatField(default=0, null=False)
    err=models.FloatField(default=0, null=False)
    froot=models.FloatField(default=0, null=False)
    date_use=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.root