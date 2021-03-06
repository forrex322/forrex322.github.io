# Generated by Django 3.2.5 on 2021-08-07 12:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210730_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Surname')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone number')),
                ('address', models.CharField(max_length=20, verbose_name='Address')),
                ('status', models.CharField(choices=[('new', 'New order'), ('in_progress', 'Order in processing'), ('is_ready', 'Order is ready'), ('completed', 'Order completed')], default='new', max_length=100, verbose_name='Status of order')),
                ('baying_type', models.CharField(choices=[('self', 'Samovuvoz'), ('delivery', 'Delivery')], default='self', max_length=100, verbose_name='Type of order')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment for order')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Data created order')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Data when order was geted')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='mainapp.customer', verbose_name='Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='mainapp.Order', verbose_name='Orders of customer'),
        ),
    ]
