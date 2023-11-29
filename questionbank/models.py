from django.db import models
from django.urls import reverse
# Create your models here.
class Question(models.Model):
    questionname = models.CharField(max_length=300)
    id=models.IntegerField(null=False,default=1,primary_key=True)
    a = models.CharField(max_length=150,null=True)
    b = models.CharField(max_length=150,null=True)
    c = models.CharField(max_length=150,null=True)
    d = models.CharField(max_length=150,null=True)
    answer = models.CharField(max_length=1,default='a',null=True)
    def __str__(self):
        return self.questionname
    def get_absolute_url(self):
        return reverse('questionbank_app:list')