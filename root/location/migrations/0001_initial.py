# Generated by Django 3.1.2 on 2020-11-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('x_coor', models.DecimalField(decimal_places=10, max_digits=50)),
                ('y_coor', models.DecimalField(decimal_places=10, max_digits=50)),
            ],
        ),
    ]
