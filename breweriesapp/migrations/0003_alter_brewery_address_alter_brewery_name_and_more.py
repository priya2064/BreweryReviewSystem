# Generated by Django 4.2.11 on 2024-06-24 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breweriesapp', '0002_brewpub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='review',
            name='brewery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='breweriesapp.brewery'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
