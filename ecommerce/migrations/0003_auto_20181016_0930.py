# Generated by Django 2.1.1 on 2018-10-16 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20181015_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageelement',
            name='image',
            field=models.ImageField(blank=True, default='media/placeholder-image.jpg', upload_to='media/'),
        ),
    ]