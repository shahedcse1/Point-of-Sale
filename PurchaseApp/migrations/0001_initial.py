# Generated by Django 4.0 on 2022-01-02 07:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SupplierApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('purchase_no', models.CharField(max_length=50)),
                ('discount', models.CharField(default=0, max_length=50, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('receiver_type', models.CharField(choices=[('Received', 'Received'), ('Not Received', 'Not Received')], default='Received', max_length=50)),
                ('order_note', models.TextField(blank=True)),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('supplier', models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_suplliar', to='SupplierApp.supplier')),
            ],
        ),
    ]
