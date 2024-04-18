# Generated by Django 4.2.11 on 2024-04-18 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='sneakers/')),
                ('price', models.FloatField(default=0.0)),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Discount %')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='goods.product')),
            ],
            options={
                'verbose_name_plural': 'Product shots',
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('remains', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(to='goods.productcolor'),
        ),
        migrations.AddField(
            model_name='product',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.style'),
        ),
    ]
