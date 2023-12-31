from django.db import models
from django.contrib.auth.models import User

class BisectOutput(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank=True)
    
    #Inputs
    f_s=models.CharField(max_length=200, null=False)    
    a=models.FloatField(default=0,null=False)
    b=models.FloatField(default=1,null=False)
    tolerance=models.FloatField(default=1e-5,null=False)
    
    #Outputs
    root=models.FloatField(default=0, null=True)
    err=models.FloatField(default=0, null=True)
    froot=models.FloatField(default=0, null=True)
    kind=models.CharField(max_length=200,default="BISECT", null=False)
    def __str__(self):
        return f"kind: {self.kind} - function: {self.f_s} - a: {self.a} - b: {self.b} - tolerance: {self.tolerance} - root: {str(self.root)}"