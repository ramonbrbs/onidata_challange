from django.contrib import admin
from contracts.models import Contract
from payments.models import Payment


class PaymentsInline(admin.TabularInline):
    model = Payment
    readonly_fields = ('amount', 'date')
    extra = 0
    can_delete = False
    max_num = 0




@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'amount', 'amount_due', 'interest_rate', 'bank']
    inlines = [PaymentsInline,]




