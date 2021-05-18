# Generated by Django 3.2 on 2021-05-15 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStamp', models.DateTimeField(verbose_name='Time when added')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(verbose_name='Current base MRP')),
                ('visibleToCostumer', models.BooleanField(verbose_name='should costumer see or not')),
                ('profitPercentage', models.FloatField(verbose_name='Profit ratio')),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]