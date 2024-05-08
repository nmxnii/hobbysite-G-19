# Generated by Django 5.0.2 on 2024-05-08 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0002_product_owner_product_status_product_stock_and_more'),
        ('user_management', '0002_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-createdOn']},
        ),
        migrations.AlterField(
            model_name='product',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='user_management.profile'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
