from django.db import models


# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_head

    item_head = models.CharField(max_length=50)
    item_title = models.CharField(max_length=50)
    item_descript = models.CharField(max_length=500)
