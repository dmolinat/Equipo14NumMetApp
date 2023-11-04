from django.db import models
from django.contrib.auth.models import User

class NumericalMethod(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank=True)
    
    #Inputs
    inputs=models.JSONField(default={}, null=False)
    
    #Outputs
    outputs=models.JSONField(default={},null=False)
    
    #Kind of method.
    kind=models.CharField(default="",null=False)
        
    date_use=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"kind: {self.kind}"