# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_added', models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)),
                ('last_changed', models.DateTimeField(verbose_name='Ultima modificação', auto_now=True)),
                ('full_name', models.CharField(verbose_name='Nome completo', max_length=150, default='')),
                ('prefered_name', models.CharField(verbose_name='Apelido', max_length=150, blank=True, null=True, default='')),
                ('email', models.EmailField(verbose_name='E-mail', max_length=150, unique=True, default='')),
                ('is_active', models.BooleanField(verbose_name='Ativo', default=True)),
                ('balance', models.DecimalField(verbose_name='Saldo em conta', default=0, max_digits=11, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Jogadore',
                'verbose_name_plural': 'Jogadores',
            },
        ),
        migrations.CreateModel(
            name='PlayerSale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_added', models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)),
                ('last_changed', models.DateTimeField(verbose_name='Ultima modificação', auto_now=True)),
                ('kind', models.CharField(verbose_name='Tipo de transação', max_length=1, default='C', choices=[('C', 'Crédito'), ('D', 'Débito')])),
                ('value', models.DecimalField(verbose_name='Valor', max_digits=11, decimal_places=2)),
                ('customer', models.ForeignKey(verbose_name='Jogadores', related_name='player_list', to='core.Customer')),
            ],
            options={
                'verbose_name': 'Extrato',
                'verbose_name_plural': 'Extratos',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('date_added', models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)),
                ('last_changed', models.DateTimeField(verbose_name='Ultima modificação', auto_now=True)),
                ('full_name', models.CharField(verbose_name='Nome completo', max_length=100, default='')),
                ('email', models.EmailField(max_length=100, unique=True, default='')),
                ('is_active', models.BooleanField(verbose_name='É ativo', default=True)),
                ('is_admin', models.BooleanField(verbose_name='É admin', default=False)),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(to='core.User'),
        ),
    ]
