from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name='User')
    product = models.ForeignKey('contents.Content', on_delete=CASCADE, verbose_name='Product')
    comment = models.TextField(verbose_name='Comment')
    email = models.CharField(verbose_name='Email')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='Register_Date')


    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = 'Order_table'
        verbose_name = 'Order'
        verbose_name_plural = 'Order'