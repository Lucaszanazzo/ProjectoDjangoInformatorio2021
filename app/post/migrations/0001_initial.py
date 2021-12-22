# Generated by Django 3.2.9 on 2021-12-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripción')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('cuerpo', models.TextField(max_length=255, verbose_name='Cuerpo')),
                ('img', models.URLField(max_length=255)),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No publicado')),
                ('categoria', models.ForeignKey(on_delete=models.SET(0), to='categoria.categoria')),
            ],
            options={
                'ordering': ('fecha_creacion',),
            },
        ),
    ]