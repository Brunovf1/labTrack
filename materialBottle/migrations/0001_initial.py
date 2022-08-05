# Generated by Django 3.2 on 2022-08-05 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=8, unique=True)),
                ('bt_type', models.CharField(choices=[('Garrafa', 'Garrafa Ambar 1l'), ('Seringa', 'Seringa 50ml')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=8, unique=True)),
                ('name', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_type', models.CharField(choices=[('GAS', 'Amostra para Analise de Gases'), ('Fisio-Quimi', 'Amostra para Analise de Fisico-Quimica'), ('2Fal', 'Amostra para Analise 2Fal')], max_length=40)),
                ('sp_time', models.DateTimeField(auto_now=True)),
                ('sp_batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialBottle.batch')),
                ('sp_bottle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materialBottle.bottle')),
                ('sp_machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialBottle.machine')),
            ],
        ),
    ]