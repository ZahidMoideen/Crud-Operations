# Generated by Django 3.2.18 on 2023-06-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=90)),
                ('password', models.CharField(max_length=90)),
            ],
        ),
    ]
