# Generated by Django 4.1.4 on 2022-12-09 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='produto',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]