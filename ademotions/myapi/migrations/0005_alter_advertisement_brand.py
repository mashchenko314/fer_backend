# Generated by Django 3.2.9 on 2022-05-17 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_alter_advertisement_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='brand',
            field=models.CharField(max_length=30, verbose_name='Бренд'),
        ),
    ]