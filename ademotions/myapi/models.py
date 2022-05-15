from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=15, verbose_name='Название')
    brand = models.CharField(max_length=20, verbose_name='Бренд')
    description = models.TextField(verbose_name='Описание', default='Описание отсутствует',null=True)
    duration = models.IntegerField(max_length=15, verbose_name='Длительность', default=0)
    url = models.CharField(max_length=10, verbose_name='Ссылка на просмотр', unique=True)
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    is_available = models.BooleanField(default=False, verbose_name='Доступность')
    video = models.FileField(upload_to='video/', verbose_name='Видео')
    screensaver = models.FileField(upload_to='screensavers/', verbose_name='Заставка')
    #user = models.CharField(max_length=20, verbose_name='Пользователь', default=None, null=True)


class Respondent(models.Model):
    name = models.CharField(max_length=15, verbose_name='Имя')
    view_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')
    record = models.FileField(upload_to='records/', verbose_name='Запись')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)