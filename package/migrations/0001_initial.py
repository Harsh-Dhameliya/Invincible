# Generated by Django 5.0.7 on 2025-01-29 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_rename_category_name_category_category_name'),
        ('hotel', '0001_initial'),
        ('transportation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(default=None, max_length=30)),
                ('p_price', models.IntegerField(default=None)),
                ('p_duration', models.CharField(default=None, max_length=40)),
                ('p_description', models.TextField(default=None)),
                ('p_image1', models.FileField(default=None, max_length=250, null=True, upload_to='package/')),
                ('p_image2', models.FileField(default=None, max_length=250, null=True, upload_to='package/')),
                ('p_image3', models.FileField(default=None, max_length=250, null=True, upload_to='package/')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Package', to='category.category')),
                ('h_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Package', to='hotel.hotel')),
                ('t_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Package', to='transportation.transportation')),
            ],
        ),
    ]
