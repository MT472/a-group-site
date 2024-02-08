from django.db import models


class account(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    password=models.CharField(max_length=250)
    password2=models.CharField(max_length=250)

    def __str__(self):
        return self.name