# Generated by Django 4.0 on 2022-07-16 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_product_name_payment_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='user_id',
            new_name='user',
        ),
    ]
