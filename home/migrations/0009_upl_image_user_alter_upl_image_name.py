# Generated by Django 4.1.7 on 2023-03-31 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_remove_upl_image_user_alter_upl_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='upl_image',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='upl_image',
            name='name',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
