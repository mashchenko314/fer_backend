# Generated by Django 3.2.9 on 2022-05-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0011_rename_advertisement_result_respondent'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='is_process',
            field=models.BooleanField(default=False, verbose_name='Обрабатывается'),
        ),
    ]
