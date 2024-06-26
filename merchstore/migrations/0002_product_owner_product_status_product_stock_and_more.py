# Generated by Django 5.0.2 on 2024-05-03 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0001_initial'),
        ('user_management', '0002_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='product', to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('On Sale', 'On Sale'), ('Out of Stock', 'Out of Stock')], default='Available', max_length=25),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='merchstore.producttype'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('On cart', 'On cart'), ('To Pay', 'To Pay'), ('To Ship', 'To Ship'), ('To Receive', 'To Receive'), ('Delivered', 'Delivered')], default=False, max_length=25)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to='user_management.profile')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='merchstore.product')),
            ],
        ),
    ]
