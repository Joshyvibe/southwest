# Generated by Django 3.1.8 on 2023-02-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20230218_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
