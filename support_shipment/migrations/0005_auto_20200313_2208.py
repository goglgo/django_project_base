# Generated by Django 3.0.4 on 2020-03-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_shipment', '0004_auto_20200313_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationmodel',
            name='district_name',
        ),
        migrations.AddField(
            model_name='shipment_ordermodel',
            name='district_name',
            field=models.CharField(default=1, max_length=10, verbose_name='동'),
            preserve_default=False,
        ),
    ]
