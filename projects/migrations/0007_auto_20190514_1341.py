# Generated by Django 2.1 on 2019-05-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20190514_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='donors',
            field=models.ManyToManyField(blank=True, related_name='donors', to='projects.Donors'),
        ),
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='images', to='projects.PImages'),
        ),
        migrations.AlterField(
            model_name='project',
            name='rates',
            field=models.ManyToManyField(blank=True, related_name='rates', to='projects.Rates'),
        ),
        migrations.AlterField(
            model_name='project',
            name='reports',
            field=models.ManyToManyField(blank=True, related_name='reports', to='projects.Reports'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='projects.Category'),
        ),
    ]
