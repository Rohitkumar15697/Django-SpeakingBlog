from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blogpost(models.Model):
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    topic=models.CharField(max_length=122,null=True,blank=False)
    title=models.CharField(max_length=250,blank=False)
    post=models.TextField()
    date=models.DateField()


    def __str__(self):
        return ' (' +str(self.created_by)+') Title- '+self.title
