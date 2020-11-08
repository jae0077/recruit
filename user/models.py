from django.db import models

class user(models.Model):
    user_type = models.IntegerField()
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=50)
    user_name = models.CharField(max_length=20)
    user_adress = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
