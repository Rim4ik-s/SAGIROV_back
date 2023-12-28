from django.db import models

# Create your models here.

class HeaderLink(models.Model):
    endpoint = models.TextField()
    text = models.TextField()


class AdvantageItem(models.Model):
    first_text = models.TextField()
    main_text = models.TextField()
    second_text = models.TextField()
    position = models.IntegerField()