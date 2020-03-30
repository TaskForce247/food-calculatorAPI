# Generated by Django 3.0.4 on 2020-03-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='calories',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='item_number',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='macro_carbohydrates',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='macro_fat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='macro_protein',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='price',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='shop',
            field=models.CharField(default='billa', max_length=100),
        ),
    ]
