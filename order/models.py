from django.db import models


class Article(models.Model):
    title = models.CharField('Заказ', max_length=50)
    anons = models.CharField('Пожелания к заказу', max_length=250)
    full_text = models.TextField('Заказ')
    publish_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/order/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Заказы'

