# Generated by Django 3.1.1 on 2021-03-16 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seminar', '0003_seminarcustomer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminarcustomer',
            name='backup_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
