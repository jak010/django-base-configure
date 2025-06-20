from django.db import models


# Create your models here.


class Sample(models.Model):
    sample_id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=100)
