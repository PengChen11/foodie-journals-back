# Generated by Django 3.0.8 on 2020-07-20 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200720_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='img_src_1',
            field=models.URLField(blank=True, max_length=2500),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img_src_2',
            field=models.URLField(blank=True, max_length=2500),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img_src_3',
            field=models.URLField(blank=True, max_length=2500),
        ),
    ]
