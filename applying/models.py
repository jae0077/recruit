from django.db import models
from user.models import user
from recruiting.models import recruiting

# Create your models here.
class applying(models.Model):
    user_num = models.ForeignKey(user, on_delete=models.CASCADE)
    recruiting_num = models.ForeignKey(recruiting, on_delete=models.CASCADE)
    status = models.IntegerField()
