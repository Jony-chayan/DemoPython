# Generated by Django 4.2.2 on 2023-07-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartoonapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartoon',
            name='img',
            field=models.ImageField(default='ddffdfs', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
