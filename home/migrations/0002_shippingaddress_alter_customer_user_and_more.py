# Generated by Django 4.2 on 2023-04-16 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to='product_images'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order'),
        ),
    ]
