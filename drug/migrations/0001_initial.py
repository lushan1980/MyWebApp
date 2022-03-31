# Generated by Django 4.0.3 on 2022-03-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=220)),
                ('time', models.IntegerField()),
                ('PC_healthxp', models.FloatField()),
                ('PC_GDP', models.FloatField()),
                ('Flag_codes', models.CharField(max_length=220)),
                ('Total_spend', models.FloatField()),
            ],
        ),
    ]
