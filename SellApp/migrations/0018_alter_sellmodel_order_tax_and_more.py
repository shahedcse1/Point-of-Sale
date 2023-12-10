# Generated by Django 4.0 on 2022-01-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellApp', '0017_alter_sellmodel_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellmodel',
            name='order_tax',
            field=models.CharField(choices=[('No tax', 'No tax'), ('VAT @10%', 'VAT @10%'), ('GST @5%', 'GST @5%')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sellmodel',
            name='payment_status',
            field=models.CharField(choices=[('Dew', 'Dew'), ('Pending', 'Pending'), ('Payment', 'Payment')], max_length=50),
        ),
    ]
