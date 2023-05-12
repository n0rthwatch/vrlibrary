from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название жанра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default=None)

    def __str__(self):
        return self.user.username if self.user else ""


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    pages_count = models.IntegerField(default=1, verbose_name='Количество страниц')
    downloads_count = models.IntegerField(default=0, verbose_name='Количество скачиваний')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateField(verbose_name='Дата создания', default='01.01.1999')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default='', null=True, verbose_name='Автор')
    image = models.ImageField(upload_to='images/books/', default='images/default_image.png', verbose_name='Изображение')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    file = models.FileField(verbose_name='Файл книги', upload_to='book_files/', null=True, default='loremka.pdf')
    user_favorites = models.ManyToManyField('Profile', verbose_name='В избранном', related_name='favorite_books')
    favorites = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books")
    alreadyFavorited = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} liked {self.book}"


class News(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    date = models.DateField(verbose_name='Дата события')
    description = models.TextField(verbose_name='Содержание')
    image = models.ImageField(verbose_name='Изображение', upload_to='images/news/',
                              default='images/news/default_image.png')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
