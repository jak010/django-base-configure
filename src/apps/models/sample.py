from django.db import models

from .abstract import TimestampModel


class Sample(TimestampModel):
    class Meta:
        db_table = "sample"

    sample_id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=100)
