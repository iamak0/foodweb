# Generated by Django 2.2 on 2023-02-10 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_items_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='prodt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]