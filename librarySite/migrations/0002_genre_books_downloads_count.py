# Generated by Django 4.1.7 on 2023-04-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarySite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название жанра')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='downloads_count',
            field=models.IntegerField(default=0, verbose_name='Количество скачиваний'),
        ),
    ]
