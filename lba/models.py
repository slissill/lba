from django.db import models


# Create your models here.
class Artist(models.Model):
    code = models.CharField(max_length=100, verbose_name="Code")
    name = models.CharField(max_length=100, verbose_name="Nom")

    def __str__(self):
        return self.name











'''
python manage.py makemigrations lba

python manage.py sqlmigrate lab 0001

python manage.py migrate
'''