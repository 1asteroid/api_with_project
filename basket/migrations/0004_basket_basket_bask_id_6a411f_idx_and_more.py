# Generated by Django 5.0.4 on 2024-05-12 13:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_alter_basket_options_alter_basketitems_options'),
        ('product', '0004_category_product_cat_id_37f831_idx_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='basket',
            index=models.Index(fields=['id'], name='basket_bask_id_6a411f_idx'),
        ),
        migrations.AddIndex(
            model_name='basketitems',
            index=models.Index(fields=['id'], name='basket_bask_id_e3c9da_idx'),
        ),
    ]
