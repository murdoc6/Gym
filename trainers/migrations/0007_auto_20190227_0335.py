# Generated by Django 2.1.5 on 2019-02-27 06:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0006_auto_20190227_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=1000, verbose_name='Content'),
        ),
    ]
