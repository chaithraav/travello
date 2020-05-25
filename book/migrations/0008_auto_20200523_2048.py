# Generated by Django 3.0.3 on 2020-05-23 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20200522_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='UPI',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='online',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='pay',
        ),
        migrations.AddField(
            model_name='payment',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='card',
            field=models.CharField(choices=[('debit', 'debit'), ('credit', 'credit')], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_no',
            field=models.CharField(default=None, max_length=14),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cvv',
            field=models.CharField(default=None, max_length=3),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expiry',
            field=models.CharField(default=None, max_length=5),
        ),
    ]
