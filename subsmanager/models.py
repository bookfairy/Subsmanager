from django.db import models
from datetime import datetime, timedelta
# from django.contrib.auth.models import User
# , on_delete=models.CASCADE

# Create your models here.


class Sub(models.Model):
    image = models.ImageField()
    name = models.TextField(max_length='50')
    link = models.TextField()
    
    def __str__(self):
        return self.name
    

class Custom(models.Model):
    sub = models.ForeignKey(Sub, on_delete=models.CASCADE)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    period = models.IntegerField()
    price = models.IntegerField()
    last_pay = models.DateField()
    
