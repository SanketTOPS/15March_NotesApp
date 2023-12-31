# Generated by Django 4.2.2 on 2023-07-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('query', models.CharField(max_length=100)),
                ('option', models.CharField(max_length=100)),
                ('files', models.FileField(upload_to='NotesFiles')),
                ('comments', models.TextField()),
            ],
        ),
    ]
