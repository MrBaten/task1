# Generated by Django 4.2.4 on 2023-09-03 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='trade_code',
            field=models.CharField(max_length=10),
        ),
    ]
