from django.db import models
from django.contrib.auth.models import User

class Rk4(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank=True)
    
    #Inputs
    ED=models.CharField(max_length=500, null=False,default="t-y")    
    a=models.FloatField(null=False,default=0)
    b=models.FloatField(null=False,default=1)
    Z=models.FloatField(default=0,null=False)
    M=models.BigIntegerField(default=10,null=False)
    
    #Outputs
    X=models.CharField(default="[]", null=True,max_length=1000)
    kind=models.CharField(max_length=200,default="RK4", null=False)
    
    def __str__(self):
        return f"kind: {self.kind} - A: {self.a} - B: {self.b} - X: {self.X}."