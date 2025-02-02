# Generated by Django 5.0.7 on 2025-01-30 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='h_name',
            new_name='Hotel_name',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='p_description',
            new_name='Package_description',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='p_duration',
            new_name='Package_duration',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='p_image1',
            new_name='Package_image1',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='p_image2',
            new_name='Package_image2',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='p_image3',
            new_name='Package_image3',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='p_name',
            new_name='Package_name',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='p_price',
            new_name='Package_price',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='t_type',
            new_name='Transportation_type',
        ),
        migrations.AddField(
            model_name='package',
            name='Guid_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Package', to='guide.guide'),
        ),
    ]
