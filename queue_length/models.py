from django.db import models

# Create your models here.


class Logdata_put(models.Model):
	queue_length=models.IntegerField()
	updated_time=models.DateTimeField('queue_length', auto_now=True)
	