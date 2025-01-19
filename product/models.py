from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=99)
    active = models.BooleanField()
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
