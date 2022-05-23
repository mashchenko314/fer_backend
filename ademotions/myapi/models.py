from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=15, verbose_name='Название')
    brand = models.CharField(max_length=20, verbose_name='Бренд')
    description = models.TextField(verbose_name='Описание', default='Описание отсутствует',null=True)
    duration = models.IntegerField(verbose_name='Длительность', default=0)
    url = models.CharField(max_length=10, verbose_name='Ссылка на просмотр', unique=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    is_available = models.BooleanField(default=False, verbose_name='Доступность')
    is_analyzed = models.BooleanField(default=False, verbose_name='Проанализирована')
    video = models.FileField(upload_to='video/', verbose_name='Видео', max_length=255)
    screensaver = models.FileField(upload_to='screensavers/', verbose_name='Заставка', max_length=255)
    user = models.CharField(max_length=30, verbose_name='Пользователь', default=None, null=True)


class Respondent(models.Model):
    name = models.CharField(max_length=15, verbose_name='Имя')
    view_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')
    record = models.FileField(upload_to='records/', verbose_name='Запись')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)


class Result(models.Model):
    top_emotion = models.CharField(max_length=15, verbose_name='Преобладающая эмоция')
    shade = models.CharField(max_length=15, verbose_name='Эмоциональный отттенок')
    engagement = models.IntegerField(verbose_name='Вовлеченность', default=0)
    respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
    angry = models.IntegerField(verbose_name='Злость', default=0)
    disgust = models.IntegerField(verbose_name='Отвращение', default=0)
    fear = models.IntegerField(verbose_name='Страх', default=0)
    happy = models.IntegerField(verbose_name='Счастье', default=0)
    sad = models.IntegerField(verbose_name='Грусть', default=0)
    surprise = models.IntegerField(verbose_name='Удивление', default=0)
    neutral = models.IntegerField(verbose_name='Нейтральность', default=0)
    csv = models.FileField(upload_to='result/', verbose_name='csv', max_length=255)