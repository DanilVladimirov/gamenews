# Generated by Django 3.2.4 on 2021-06-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0008_auto_20210610_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='comments',
            field=models.ManyToManyField(blank=True, editable=False, to='newsapp.Comment'),
        ),
    ]