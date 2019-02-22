# Generated by Django 2.1.5 on 2019-02-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
                'ordering': ['title'],
            },
        ),
    ]
