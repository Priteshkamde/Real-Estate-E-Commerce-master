# Generated by Django 2.1 on 2018-09-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_delete_a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='BHK',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('>5', '>5')], max_length=10000),
        ),
        migrations.AlterField(
            model_name='properties',
            name='area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='properties',
            name='buy_rent',
            field=models.CharField(choices=[('Buy', 'Buy'), ('Rent', 'Rent')], max_length=10000),
        ),
        migrations.AlterField(
            model_name='properties',
            name='construction_status',
            field=models.CharField(choices=[('Under Construction', 'Under Construction'), ('Ready To Move', 'Ready To Move')], max_length=100),
        ),
        migrations.AlterField(
            model_name='properties',
            name='property_type',
            field=models.CharField(choices=[('Flat', 'Flat'), ('House/Villa', 'House/Villa'), ('Plot', 'Plot'), ('Office Space', 'Office Space'), ('Other Commercial', 'Other Commercial'), ('Shop/Showroom', 'Shop/Showroom'), ('PG', 'PG')], max_length=10000),
        ),
    ]
