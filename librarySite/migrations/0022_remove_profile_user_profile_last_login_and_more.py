# Generated by Django 4.1.7 on 2023-05-10 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarySite', '0021_alter_news_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default='123', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='test', max_length=50, verbose_name='Имя пользователя'),
            preserve_default=False,
        ),
    ]
