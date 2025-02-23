from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        app_label = 'mysql'
        db_table = 'users'