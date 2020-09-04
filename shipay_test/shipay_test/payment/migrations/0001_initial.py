# Generated by Django 2.2.3 on 2020-09-03 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=20)),
                ('dono', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recebimentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=20)),
                ('valor', models.FloatField()),
                ('descricao', models.CharField(max_length=255)),
                ('Estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.Estabelecimento')),
            ],
        ),
    ]