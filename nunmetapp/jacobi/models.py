from django.db import models
from django.contrib.auth.models import User

class Jacobi(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank=True)
    
    #Inputs
    A=models.CharField(max_length=500, null=False,default="[]")    
    B=models.CharField(max_length=500,null=False,default="[]")
    x0=models.CharField(max_length=500,null=False,default="[]")
    tolerance=models.FloatField(default=1e-5,null=False)
    max_iter=models.BigIntegerField(default=1,null=False)
    
    #Outputs
    X=models.CharField(default="[]", null=True,max_length=500)
    number_iteration=models.IntegerField(default=0, null=True)
    err=models.FloatField(default=0, null=True)
    kind=models.CharField(max_length=200,default="JACOBI", null=False)
    
    def __str__(self):
        return f"kind: {self.kind} - A: {self.A} - B: {self.B} - X: {self.X} - Max_Iteration: {self.number_iteration} - error: {str(self.err)}"