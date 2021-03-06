# Generated by Django 2.1.5 on 2019-02-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('department', models.CharField(choices=[('1', 'Dep1'), ('2', 'Dep2'), ('3', 'Dep3')], max_length=1)),
                ('hiredDate', models.DateField()),
                ('isPermanent', models.BooleanField()),
            ],
        ),
    ]
