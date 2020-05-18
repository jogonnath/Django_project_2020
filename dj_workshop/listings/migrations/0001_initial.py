# Generated by Django 2.2.10 on 2020-05-02 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zipcode', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=150, verbose_name='Description')),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('garage', models.BooleanField()),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_published', models.BooleanField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo1', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo2', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo3', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo4', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo5', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo6', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtors.Realtor')),
            ],
        ),
    ]
