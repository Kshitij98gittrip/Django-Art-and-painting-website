# Generated by Django 4.1.7 on 2023-03-30 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_remove_upl_image_socialmedia_upl_image_fb_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='upl_image',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
