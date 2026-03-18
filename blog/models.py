from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text= 'Введите заголовок поста')
    content = models.TextField(verbose_name='Содержимое поста', null=True, blank=True, help_text='Напишите содержимое поста')
    image = models.ImageField(upload_to='blog/images',null=True, blank=True, verbose_name='Превью поста')
    created_at = models.DateTimeField(auto_now_add=True)
    is_publishing = models.BooleanField(verbose_name='Признак публикации', help_text='Признак публикации')
    count_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров',help_text='Количество просмотров')

    def __str__(self):
        return f'Пост: {self.title}, создан {self.created_at}. Опубликован: {self.is_publishing}. Просмотров: {self.count_views}.'

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['created_at',]
