# Generated by Django 3.2.4 on 2021-06-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='comments',
            field=models.ManyToManyField(blank=True, to='newsapp.Comment'),
        ),
    ]