from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'users'