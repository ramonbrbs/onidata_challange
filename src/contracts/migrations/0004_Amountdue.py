# Generated by Django 2.2.2 on 2019-06-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_Amount_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='amount_due',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Amount Due'),
            preserve_default=False,
        ),
    ]
