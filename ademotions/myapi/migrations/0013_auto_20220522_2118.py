# Generated by Django 3.2.9 on 2022-05-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0012_advertisement_is_process'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='is_process',
        ),
        migrations.AddField(
            model_name='result',
            name='angry',
            field=models.IntegerField(default=0, verbose_name='Злость'),
        ),
        migrations.AddField(
            model_name='result',
            name='csv',
            field=models.FileField(default=0, max_length=255, upload_to='result/', verbose_name='csv'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='disgust',
            field=models.IntegerField(default=0, verbose_name='Отвращение'),
        ),
        migrations.AddField(
            model_name='result',
            name='fear',
            field=models.IntegerField(default=0, verbose_name='Страх'),
        ),
        migrations.AddField(
            model_name='result',
            name='happy',
            field=models.IntegerField(default=0, verbose_name='Счастье'),
        ),
        migrations.AddField(
            model_name='result',
            name='neutral',
            field=models.IntegerField(default=0, verbose_name='Нейтральность'),
        ),
        migrations.AddField(
            model_name='result',
            name='sad',
            field=models.IntegerField(default=0, verbose_name='Грусть'),
        ),
        migrations.AddField(
            model_name='result',
            name='surprise',
            field=models.IntegerField(default=0, verbose_name='Удивление'),
        ),
    ]
