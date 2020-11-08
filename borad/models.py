from django.db import models
from user.models import user

# Create your models here.
class borad(models.Model):
    user_num = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
    borad_title = models.CharField(max_length=100)
    borad_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
