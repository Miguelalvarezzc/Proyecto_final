# Generated by Django 4.2.4 on 2023-10-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0003_alter_avatar_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('autor', models.CharField(max_length=70)),
            ],
        ),
    ]
