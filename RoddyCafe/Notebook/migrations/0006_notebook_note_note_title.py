# Generated by Django 4.0.3 on 2022-04-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0005_remove_notebook_note_note_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook_note',
            name='note_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='笔记标题'),
        ),
    ]
