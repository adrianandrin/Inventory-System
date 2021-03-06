# Generated by Django 3.1.1 on 2020-10-05 05:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('middlename', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phoneNumber', models.IntegerField()),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=30)),
                ('size', models.FloatField()),
                ('price', models.FloatField()),
                ('no_stocks', models.IntegerField()),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.person')),
                ('profile', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Customer',
            },
            bases=('dashboard.person',),
        ),
    ]
