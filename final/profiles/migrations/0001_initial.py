# Generated by Django 3.1.7 on 2021-04-01 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('Accno', models.IntegerField(primary_key=True, serialize=False)),
                ('Balance', models.FloatField()),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Cust_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Phone_no', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('Trans_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('Type', models.CharField(max_length=30)),
                ('Accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.account')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='Money_Transfers',
            fields=[
                ('Trans_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('From_accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From_accno', to='profiles.account')),
                ('To_accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To_accno', to='profiles.account')),
            ],
            options={
                'db_table': 'transfers',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.customer'),
        ),
    ]