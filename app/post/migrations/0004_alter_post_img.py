# Generated by Django 3.2.9 on 2021-12-04 17:23

import app.post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post/infoblog-logo.png', upload_to=app.post.models.Post.user_directory_path),
        ),
    ]