# Generated by Django 5.1.1 on 2024-10-18 14:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_remove_comment_text_comment_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]