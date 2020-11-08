from django.db import models
from user.models import user

# Create your models here.
class resume(models.Model):
    user_num = models.ForeignKey(user, on_delete=models.CASCADE)
    resume_title = models.CharField(max_length=100)
    resume_content = models.TextField()
