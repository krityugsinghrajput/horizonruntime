# Generated by Django 4.1 on 2022-09-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debugfinder', '0003_bookstore'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstore',
            name='information',
            field=models.CharField(default='Hello world', max_length=255),
            preserve_default=False,
        ),
    ]
