from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Name of product')),
                ('slug', models.SlugField(max_length=256)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Image')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('diagonal', models.CharField(max_length=256, verbose_name='Diagonal')),
                ('display', models.CharField(max_length=256, verbose_name='Display')),
                ('resolution', models.CharField(max_length=256, verbose_name='Resolution')),
                ('accum_volume', models.CharField(max_length=256, verbose_name='Accumulator')),
                ('ram', models.CharField(max_length=256, verbose_name='Ram')),
                ('sd', models.BooleanField(default=True)),
                ('sd_volume_max', models.CharField(max_length=256, verbose_name='Maximum internal memory ')),
                ('main_cam_mp', models.CharField(max_length=256, verbose_name='Megapixels of main camera')),
                ('front_cam_mp', models.CharField(max_length=256, verbose_name='Megapixels of frontal camera')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Name of product')),
                ('slug', models.SlugField(max_length=256)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Image')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('diagonal', models.CharField(max_length=256, verbose_name='Diagonal')),
                ('display', models.CharField(max_length=256, verbose_name='Display')),
                ('processor_freq', models.CharField(max_length=256, verbose_name='Processor freq')),
                ('ram', models.CharField(max_length=256, verbose_name='Ram')),
                ('video', models.CharField(max_length=256, verbose_name='Graphic card')),
                ('time_without_charge', models.CharField(max_length=256, verbose_name='Time of work accumulator')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]