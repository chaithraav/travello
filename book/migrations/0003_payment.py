# Generated by Django 3.0.3 on 2020-05-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(choices=[('debit', 'debit'), ('credit', 'credit')], max_length=20)),
                ('card_no', models.IntegerField(max_length=14)),
                ('cvv', models.IntegerField(max_length=3)),
                ('expiry', models.CharField(max_length=5)),
                ('online', models.CharField(choices=[('Gpay', 'Gpay'), ('paytm', 'paytm'), ('phonepay', 'phonepay')], max_length=20)),
                ('upi', models.IntegerField(max_length=6)),
            ],
        ),
    ]