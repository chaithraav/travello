# Generated by Django 3.0.3 on 2020-05-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20200519_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card',
            field=models.CharField(blank=True, choices=[('debit', 'debit'), ('credit', 'credit')], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_no',
            field=models.CharField(blank=True, default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expiry',
            field=models.CharField(blank=True, default=None, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='online',
            field=models.CharField(blank=True, choices=[('Gpay', 'Gpay'), ('paytm', 'paytm'), ('phonepay', 'phonepay')], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pay',
            field=models.CharField(choices=[('card', 'card'), ('online', 'online')], default=None, max_length=10),
        ),
    ]