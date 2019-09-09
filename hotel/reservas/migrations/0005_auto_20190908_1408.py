# Generated by Django 2.2.4 on 2019-09-08 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0004_auto_20190907_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookingtype_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reservas.BookingType'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.Perfil'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reservas.Room'),
        ),
    ]
