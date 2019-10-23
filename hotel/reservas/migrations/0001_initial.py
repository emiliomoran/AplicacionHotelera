# Generated by Django 2.2.4 on 2019-10-13 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accesos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('is_removed', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('is_removed', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=200)),
                ('eliminado', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion del Cuarto')),
                ('path_image', models.FileField(null=True, upload_to='rooms/', verbose_name='Url de Imagen')),
                ('calificacion', models.IntegerField(default=0, verbose_name='Calificacion')),
                ('num_camas', models.IntegerField(default=0, verbose_name='Numero de Camas')),
                ('num_adultos', models.IntegerField(default=0, verbose_name='Numero de Adultos')),
                ('num_ninos', models.IntegerField(default=0, verbose_name='Numero de Niños')),
                ('precio', models.FloatField(default=0, verbose_name='Precio')),
                ('disponible', models.BooleanField(default=True)),
                ('eliminado', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('id_roomtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.RoomType', verbose_name='Tipo de Cuarto')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('check_in_date', models.DateTimeField(null=True)),
                ('check_out_date', models.DateTimeField(null=True)),
                ('no_nights', models.IntegerField(default=0)),
                ('is_removed', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('bookingtype_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.BookingType')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.Perfil')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.Room')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.BookingState')),
            ],
        ),
    ]
