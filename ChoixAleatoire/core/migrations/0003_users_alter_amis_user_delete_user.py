# Generated by Django 4.1.6 on 2023-02-15 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_amis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='amis',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.users'),
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
