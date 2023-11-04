from django.db import models
from django.contrib.auth.models import User

class BoolerlOutput(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank=True)
    
    #Inputs
    f_s=models.CharField(max_length=200, null=False)    
    a=models.IntegerField(default=0,null=False)
    b=models.IntegerField(default=1,null=False)
    M=models.BigIntegerField(default=4,null=False)
    
    #Outputs
    aprox=models.FloatField(default=0,null=False)
    kind=models.CharField(default="BOOLERL", null=False)
    
    def __str__(self):
        return f"kind: {self.kind} - function: {self.f_s} - a: {self.a} - b: {self.b} - M: {self.M} - Aprox: {str(self.aprox)}"