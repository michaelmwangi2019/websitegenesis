# Generated by Django 2.2.7 on 2019-11-20 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicationtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Middle_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=6)),
                ('Applicant_ID', models.IntegerField(unique=True)),
                ('Amount', models.IntegerField()),
                ('Birth_Date', models.DateField()),
                ('Guardian_Telephone', models.IntegerField(default=0)),
                ('Institution_Name', models.CharField(max_length=254, null=True)),
                ('Application_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Disbursementtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount_Disbursed', models.IntegerField()),
                ('Disbursement_No', models.IntegerField(unique=True)),
                ('Disbursement_Date', models.DateField()),
                ('Applicant_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.Applicationtable')),
            ],
        ),
    ]
