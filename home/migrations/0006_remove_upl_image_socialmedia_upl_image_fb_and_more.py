# Generated by Django 4.1.7 on 2023-03-29 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_upl_image_desc_remove_upl_image_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upl_image',
            name='socialmedia',
        ),
        migrations.AddField(
            model_name='upl_image',
            name='fb',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upl_image',
            name='insta',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upl_image',
            name='otherlink',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
    ]
