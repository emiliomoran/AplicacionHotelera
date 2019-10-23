# Generated by Django 2.2.4 on 2019-10-13 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accesos', '0001_initial'),
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('reserva', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservas.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_code', models.CharField(max_length=12)),
                ('is_ordered', models.BooleanField(default=True)),
                ('items', models.ManyToManyField(to='shopping_cart.OrderItem')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accesos.Perfil')),
            ],
        ),
    ]
