# Generated by Django 4.0 on 2022-01-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='', upload_to='user_images/'),
            preserve_default=False,
        ),
    ]
