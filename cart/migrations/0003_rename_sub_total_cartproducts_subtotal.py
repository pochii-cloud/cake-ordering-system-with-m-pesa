# Generated by Django 4.0.4 on 2022-05-02 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_total_cart_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartproducts',
            old_name='sub_total',
            new_name='subtotal',
        ),
    ]
