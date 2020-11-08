from django.db import models
from user.models import user
from borad.models import borad

# Create your models here.
class comment(models.Model):
    user_num = models.ForeignKey(user, on_delete=models.CASCADE)
    borad_num = models.ForeignKey(borad, on_delete=models.CASCADE)
    comment_content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
