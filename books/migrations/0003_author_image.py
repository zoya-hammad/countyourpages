# Generated by Django 5.0.4 on 2024-05-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(default='images/authors/default.jpg', upload_to='images/authors'),
            preserve_default=False,
        ),
    ]
