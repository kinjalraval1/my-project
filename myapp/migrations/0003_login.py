# Generated by Django 4.0 on 2022-01-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
