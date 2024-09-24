# Generated by Django 5.1.1 on 2024-09-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='det',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('par', models.TextField()),
                ('im', models.ImageField(upload_to='Gallery')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
