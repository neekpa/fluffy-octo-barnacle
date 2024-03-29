# Generated by Django 2.2.6 on 2019-10-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=20)),
                ('Type', models.CharField(choices=[('VEHICLE', 'veh'), ('DUSTBIN', 'dust')], max_length=2)),
                ('Device_use', models.CharField(max_length=1)),
                ('Quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'device',
            },
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=20)),
                ('Email_id', models.CharField(max_length=20)),
                ('adhar_card_no', models.IntegerField()),
                ('Front_A', models.ImageField(upload_to='front/')),
                ('Back_A', models.ImageField(upload_to='back/')),
                ('Driving_lisence_no', models.IntegerField()),
                ('Front_L', models.ImageField(upload_to='front/')),
                ('Back_L', models.ImageField(upload_to='back/')),
                ('Date_of_expiry', models.IntegerField()),
                ('contact_no', models.IntegerField()),
            ],
            options={
                'db_table': 'driver',
            },
        ),
        migrations.CreateModel(
            name='Dustbin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dustbin_no', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('expiry', models.IntegerField()),
                ('comment', models.TextField(max_length=500)),
                ('location', models.CharField(max_length=40)),
                ('RFID_TAG', models.IntegerField()),
            ],
            options={
                'db_table': 'Dustbin',
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('adhar_card_no', models.CharField(max_length=12)),
                ('service_type', models.CharField(max_length=3)),
                ('contact_no', models.IntegerField()),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('Mini', 'mini'), ('MICRO', 'micro'), ('SEDAN', 'sedan'), ('SUV', 'suv')], max_length=20)),
                ('capacity', models.IntegerField()),
                ('area', models.IntegerField()),
                ('vehicle_no', models.IntegerField()),
                ('rfid_kit_no', models.IntegerField()),
            ],
            options={
                'db_table': 'vehicle',
            },
        ),
    ]
