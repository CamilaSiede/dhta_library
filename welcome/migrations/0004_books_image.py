# Generated by Django 4.0 on 2022-01-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0003_remove_books_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(default='test', upload_to='images'),
            preserve_default=False,
        ),
    ]
