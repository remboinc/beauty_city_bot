# Generated by Django 5.1.4 on 2024-12-22 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_alter_appointment_salon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='specialist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='bot.specialist'),
        ),
    ]