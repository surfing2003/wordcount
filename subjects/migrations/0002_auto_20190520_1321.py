# Generated by Django 2.0.13 on 2019-05-20 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subjects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='subjects.Subject'),
        ),
    ]