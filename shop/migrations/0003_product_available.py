# Generated by Django 2.2 on 2023-02-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]