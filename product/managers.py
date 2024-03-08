from django.db import models

class ProductManager(models.Manager):
    def product_Avalible_True(self):
        return self.filter(available=True)