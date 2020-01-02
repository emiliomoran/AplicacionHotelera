# Generated by Django 2.2.7 on 2019-12-02 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_auto_20191202_1256'),
        ('accesos', '0001_initial'),
        ('tour_package', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourOrder',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shopping_cart.Product')),
                ('reservation_name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accesos.Perfil')),
                ('tour', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour_package.Tour_Package')),
            ],
            bases=('shopping_cart.product',),
        ),
        migrations.DeleteModel(
            name='Tour_Order',
        ),
    ]