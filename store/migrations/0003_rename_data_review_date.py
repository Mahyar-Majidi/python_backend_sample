# Generated by Django 4.2.7 on 2023-12-07 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_orderitem_product_alter_product_collection_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='data',
            new_name='date',
        ),
    ]