# Generated by Django 2.1 on 2018-09-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0013_auto_20180911_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='property',
        ),
        migrations.AddField(
            model_name='comments',
            name='property_title',
            field=models.CharField(default='', max_length=10000),
            preserve_default=False,
        ),
    ]