# Generated by Django 4.0.3 on 2022-06-16 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0020_alter_note_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note_file',
            name='file',
            field=models.FileField(upload_to="Value('Notebook/user/') + F(note__user__id)", verbose_name='文件内容'),
        ),
    ]
