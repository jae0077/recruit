from django.db import models
from user.models import user
# Create your models here.
class recruiting(models.Model):
    user_num = models.ForeignKey(user, on_delete=models.CASCADE)
    recruiting_title = models.CharField(max_length=100)
    recruiting_content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
   
