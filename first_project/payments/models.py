from django.db import models


class Payments(models.Model):
    currency = models.CharField("Currency", max_length=3, unique=True)
    exchange_rete_to_usd = models.CharField("Rate", max_length=10)

    class Meta:
        verbose_name = "Payments"
        verbose_name_plural = 'Payments'
        ordering = ['currency']

    def __str__(self):
        return self.currency
