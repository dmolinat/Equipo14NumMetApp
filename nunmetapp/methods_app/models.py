from django.db import models
from django.contrib.auth.models import User
from bisect_app.models import BisectOutput
from jacobi.models import Jacobi
from boolerl_app.models import BoolerlOutput

class NumericalMethod(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank=True)
    
    #Inputs
    inputs=models.JSONField(default={'test_input': 0}, null=False)
    
    #Outputs
    outputs=models.JSONField(default={'test_output':1},null=True)
    
    #Kind of method.
    kind=models.CharField(max_length=200,default="",null=False)
    bisect = models.ForeignKey(
        BisectOutput, on_delete=models.CASCADE, null=True, blank=True
    )
    boolerl = models.ForeignKey(
        BoolerlOutput, on_delete=models.CASCADE, null=True, blank=True
    )
    jacobi = models.ForeignKey(
        Jacobi, on_delete=models.CASCADE, null=True, blank=True
    )
    
    #rk4 = models.ForeignKey(
    #    RK4, on_delete=models.CASCADE, null=True, blank=True
    #) 
    
        
    date_use=models.DateTimeField(null=True)
    def __str__(self):
        return f"kind: {self.kind}"
    
    def isBisect(self):
        return "BISECT" in self.kind
    
    def isJacobi(self):
        return "JACOBI" in self.kind
    
    def isBoolerl(self):
        return "BOOLERL" in self.kind
    
    def isRK4(self):
        return "RK4" in self.kind