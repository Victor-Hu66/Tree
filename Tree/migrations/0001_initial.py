# Generated by Django 4.0.1 on 2022-01-31 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('url_name', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Linktree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('button', models.ManyToManyField(related_name='button', to='Tree.Button')),
            ],
        ),
    ]
