# Generated by Django 4.0.4 on 2022-05-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_rename_cartproducts_cartproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='subtotal',
            field=models.PositiveIntegerField(),
        ),
    ]
