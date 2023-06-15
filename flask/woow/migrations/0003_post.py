# Generated by Django 4.1.5 on 2023-02-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woow', '0002_alter_user_message_alter_user_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('month', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=400)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
