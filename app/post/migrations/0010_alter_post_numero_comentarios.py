# Generated by Django 3.2.9 on 2021-12-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_alter_post_numero_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='numero_comentarios',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
