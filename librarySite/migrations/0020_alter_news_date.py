# Generated by Django 4.1.7 on 2023-05-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarySite', '0019_news_alter_book_image_alter_book_user_favorites_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(verbose_name='Дата события'),
        ),
    ]
