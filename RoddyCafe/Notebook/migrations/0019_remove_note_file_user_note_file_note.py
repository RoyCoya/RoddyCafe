# Generated by Django 4.0.3 on 2022-06-16 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0018_rename_content_note_file_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note_file',
            name='user',
        ),
        migrations.AddField(
            model_name='note_file',
            name='note',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Notebook.note', verbose_name='所属笔记'),
            preserve_default=False,
        ),
    ]
