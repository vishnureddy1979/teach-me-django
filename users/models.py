from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(blank=True, null=True)
    is_teacher = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
