# Generated by Django 4.0.5 on 2022-08-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esqueleto', '0009_subastarpublicacion_usuario_subasta_delete_subasta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='ImgArticulo',
            field=models.ImageField(default='Articulos/Nada.jpg', upload_to='Articulos'),
        ),
    ]
