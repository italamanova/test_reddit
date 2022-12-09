# Generated by Django 4.1.4 on 2022-12-09 15:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.URLField()),
                ('upvotes', models.PositiveSmallIntegerField(default=0)),
                ('downvotes', models.PositiveSmallIntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
