# Generated by Django 3.2.9 on 2022-05-17 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_advertisement_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='url',
            field=models.CharField(blank=True, max_length=10, unique=True, verbose_name='Ссылка на просмотр'),
        ),
    ]
