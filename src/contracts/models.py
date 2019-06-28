from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from datetime import datetime
from dateutil import relativedelta



class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField("Amount", max_digits=14, decimal_places=2)
    amount_due = models.DecimalField("Amount Due", max_digits=15, decimal_places=2, default=0)
    interest_rate = models.DecimalField("Monthly Interest Rate (percent 1 = 100%)", max_digits=8, decimal_places=5)
    ip_address = models.CharField(_("IP Submitted"), max_length=50)
    submission_date = models.DateTimeField("Submission Date", auto_now_add=True)
    bank = models.CharField("Bank Owner", max_length=50)
    customer_metadata = models.TextField("Customer Metadata", null=True,blank=True)

    def save(self, *args, **kwargs):
        if(self.pk is None):
            self.amount_due = self.amount
        super().save(*args, **kwargs)



    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reversed("contract_detail", kwargs={"pk": self.pk})

