from django.db import models
from django.utils.translation import gettext as _
from contracts.models import Contract


class Payment(models.Model):
    contract = models.ForeignKey("contracts.Contract", on_delete=models.CASCADE, related_name='payments')
    date = models.DateField(_("Payment Date"), auto_now_add=True)
    amount = models.DecimalField(_("Amount"), max_digits=14, decimal_places=2)

    def save(self, *args, **kwargs):
        print('oo')
        if(self.pk is None):
            contract = Contract.objects.get(pk=self.contract_id)
            contract.amount_due -= self.amount
            print('contrac amout --- ' + str(contract.amount))
            contract.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("payments")

    def __str__(self):
        return str(self.id)

