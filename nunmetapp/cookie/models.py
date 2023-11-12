from django.db import models
from django.contrib.auth.models import User

class UserCookie(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, null=True, blank=True)
    cookie_active = models.BooleanField(default=False)
    date_use=models.DateTimeField(null=True)
    
    def __str__(self):
        return f"user: {self.user}, cookie: {self.cookie_active}"
    
class CookieCountMethodUse(models.Model):
    method = models.CharField(default="MEHOD NAME", max_length=10)
    count = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return f"method: {self.method}, count: {self.count}"