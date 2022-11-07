from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория (ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название Тэга')
    slug = models.SlugField(max_length=50, verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название Новости')
    slug = models.SlugField(max_length=255, verbose_name='Слаг', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор поста')
    content = models.TextField(blank=True, verbose_name='Содержание статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    photo = models.ImageField(upload_to='photos/%Y%m%d/', blank=True, verbose_name='Фотография')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='posts', verbose_name='Название категории')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts',
                                  verbose_name='Название тега')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья (ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
