from django.db import models

# Create your models here.




class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self) :
        return self.name 