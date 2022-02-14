from django.db import models


class Article(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    content = models.TextField("содержание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
