# Generated by Django 2.1.1 on 2018-10-27 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombred', models.CharField(max_length=200, verbose_name='Nombre')),
                ('industria', models.CharField(max_length=200, verbose_name='Industria')),
                ('fundacion', models.CharField(max_length=200, verbose_name='fundacion')),
                ('sede', models.CharField(max_length=200, verbose_name='sede')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Distribuidora',
                'verbose_name_plural': 'Distribuidoras',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('creadores', models.CharField(max_length=200, verbose_name='creadores')),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='app', verbose_name='imagen')),
                ('Plataformas', models.CharField(max_length=200, verbose_name='Plataformas')),
                ('Descripcion', models.TextField(verbose_name='Descripcion')),
                ('fecha_lanzamiento', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de lanzamiento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('distribuidora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Distribuidora')),
                ('genero', models.ManyToManyField(to='app.Genero', verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'Juego',
                'verbose_name_plural': 'Juegos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='app', verbose_name='imagen')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
                'ordering': ['-created'],
            },
        ),
    ]