from django.core.management.base import BaseCommand, CommandError
from contracts.models import Contract
from datetime import datetime


class Command(BaseCommand):
    help = 'Increase the amount due if one month has past since the submition date'

    # TODO VALIDAR PARA MESES COM 30 E 31 DIAS, ASSIM COMO FEVEREIRO
    def handle(self, *args, **options):
        contracts = Contract.objects.all()

        for contract in contracts:
            if contract.amount_due > 0 and contract.submission_date.date() != datetime.today().date() \
                    and contract.submission_date.day == datetime.today().day:
                self.stdout.write(self.style.SUCCESS('Contract amount updated "%s"' % contract))
                contract.amount_due = contract.amount_due * contract.interest_rate
                contract.save()

        self.stdout.write(self.style.SUCCESS('Finalized increase_amount_due job'))
