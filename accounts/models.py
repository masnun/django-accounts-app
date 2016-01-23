from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.
class Account(models.Model):
    name = models.CharField("A/C Name", max_length=200)
    description = models.TextField("Description")
    balance = models.FloatField("Balance")

    def __str__(self):
        return self.name


class Transaction(models.Model):
    account = models.ForeignKey(Account)
    notes = models.CharField("Notes", max_length=200)
    debit = models.FloatField("Debit Amount")
    credit = models.FloatField("Credit Amount")
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Transaction)
def transaction_saved(sender, instance, created=False, **kwargs):
    if created:
        instance.account.balance = instance.account.balance + instance.credit - instance.debit
        instance.account.save()


@receiver(post_delete, sender=Transaction)
def transaction_deleted(sender, instance, **kwargs):
    instance.account.balance = instance.account.balance - instance.credit + instance.debit
    instance.account.save()
