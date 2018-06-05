# Generated by Django 2.0.2 on 2018-06-04 03:14

import catalogue.validators
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Titulo')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('autor', models.CharField(max_length=40, verbose_name='Autor')),
                ('quantity', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('edition', models.IntegerField(verbose_name='Edicion')),
                ('editorial', models.CharField(max_length=40, verbose_name='Editorial')),
                ('cover_page', models.ImageField(blank=True, null=True, upload_to='Profiles', validators=[catalogue.validators.validate_file_extension], verbose_name='Portada')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('ISBN', models.CharField(max_length=15, verbose_name='ISBN')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('client', models.ManyToManyField(to='registration.Profile', verbose_name='Cliente')),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['-created'],
            },
        ),
    ]