# Generated by Django 5.1 on 2024-08-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('confirmPassword', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
