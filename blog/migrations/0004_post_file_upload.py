# Generated by Django 4.2 on 2023-05-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_head_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='blog/files/%Y/%m/%d/'),
        ),
    ]