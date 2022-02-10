# Generated by Django 4.0.2 on 2022-02-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'ordering': ['date'], 'verbose_name_plural': 'Movies'},
        ),
        migrations.AddField(
            model_name='movies',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
