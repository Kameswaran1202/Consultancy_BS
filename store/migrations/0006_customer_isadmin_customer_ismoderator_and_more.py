# Generated by Django 4.1.2 on 2022-11-29 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='isadmin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='ismoderator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='isnormaluser',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
