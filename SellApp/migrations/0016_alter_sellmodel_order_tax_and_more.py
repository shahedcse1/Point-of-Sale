# Generated by Django 4.0 on 2022-01-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellApp', '0015_alter_sellmodel_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellmodel',
            name='order_tax',
            field=models.CharField(choices=[('GST @5%', 'GST @5%'), ('VAT @10%', 'VAT @10%'), ('No tax', 'No tax')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sellmodel',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Payment', 'Payment'), ('Dew', 'Dew')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sellmodel',
            name='sale_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=50),
        ),
    ]
