# Generated by Django 4.0.3 on 2022-04-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0009_remove_notebook_directory_directory_createddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook_directory',
            name='directory_discription',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='目录描述'),
        ),
    ]