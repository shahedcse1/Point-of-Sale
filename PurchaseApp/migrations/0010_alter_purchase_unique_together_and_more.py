# Generated by Django 4.0 on 2022-01-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseApp', '0009_alter_purchase_slug_alter_purchase_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='purchase',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='reference_no',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
