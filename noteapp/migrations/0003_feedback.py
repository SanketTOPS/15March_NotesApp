# Generated by Django 4.2.2 on 2023-07-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_mynotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('msg', models.TextField()),
            ],
        ),
    ]