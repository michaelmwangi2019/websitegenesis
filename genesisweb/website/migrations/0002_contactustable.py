# Generated by Django 3.1.1 on 2020-09-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactustable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('phonenum', models.IntegerField(unique=True)),
                ('county', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=254, null=True)),
                ('hearus', models.CharField(max_length=254, null=True)),
            ],
        ),
    ]
