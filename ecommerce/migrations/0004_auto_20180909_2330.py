# Generated by Django 2.1 on 2018-09-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20180909_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('seller', 'seller'), ('buyer', 'buyer')], max_length=100),
        ),
    ]