# Generated by Django 3.0.8 on 2020-07-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
