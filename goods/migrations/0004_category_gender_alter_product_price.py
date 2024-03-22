# Generated by Django 4.2.11 on 2024-03-22 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_gender_product_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='goods.gender'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
