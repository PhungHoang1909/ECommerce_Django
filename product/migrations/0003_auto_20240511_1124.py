# Generated by Django 3.2.6 on 2024-05-11 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='primary_key',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]