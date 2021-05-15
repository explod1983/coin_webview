from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=30, primary_key=True, blank=True)
    amount = models.CharField(max_length=30)
    buy_price = models.CharField(max_length=30)
    desired_price_fall = models.CharField(max_length=30)
    desired_sell_price = models.CharField(max_length=30)
    last_prices = models.TextField()

    def __str__(self):
        return self.name