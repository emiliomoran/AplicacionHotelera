# Generated by Django 2.2.4 on 2019-09-07 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_auto_20190906_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id_roomtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.RoomType'),
        ),
    ]