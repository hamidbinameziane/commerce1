from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class listing(models.Model):
    product_image: models.ImageField()
    product_name: models.CharField()
    starting_bid: models.DecimalField(max_digits=10, decimal_places=2)
    description: models.CharField()
    date_created: models.BinaryField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

class bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(listing, on_delete=models.CASCADE)

class comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(listing, on_delete=models.CASCADE)
