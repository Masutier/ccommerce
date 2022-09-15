# Generated by Django 3.1.7 on 2021-03-02 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('floor', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('localNum', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('whatsapp', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('webpage', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(default='img/logos/default.png', upload_to='img/logos')),
                ('localFoto', models.ImageField(default='img/locals/logolocal.png', upload_to='img/locals')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=False, null=True)),
                ('pay', models.CharField(blank=True, choices=[('unmes', 'Mes'), ('tresmes', 'Trimestre'), ('seismes', 'Semestre'), ('year', 'Anual')], default='En Aprobación', max_length=50, null=True)),
                ('payday', models.DateField(blank=True, null=True)),
                ('activethru', models.DateField(blank=True, null=True)),
            ],
        ),
    ]