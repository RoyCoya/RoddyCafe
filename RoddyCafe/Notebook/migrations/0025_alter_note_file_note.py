# Generated by Django 4.0.3 on 2022-06-16 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0024_alter_note_file_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note_file',
            name='note',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Notebook.note', verbose_name='所属笔记'),
            preserve_default=False,
        ),
    ]
