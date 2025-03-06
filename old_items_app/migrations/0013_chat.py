# Generated by Django 4.2.17 on 2025-01-28 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('old_items_app', '0012_mystatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_message', models.CharField(blank=True, max_length=100, null=True)),
                ('seller_message', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('customer_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='old_items_app.customer')),
                ('product_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='old_items_app.product')),
                ('seller_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='old_items_app.seller')),
            ],
        ),
    ]
