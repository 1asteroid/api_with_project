# Generated by Django 5.0.4 on 2024-05-12 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
