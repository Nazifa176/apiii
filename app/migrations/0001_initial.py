# Generated by Django 4.1.5 on 2023-02-01 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('category_icon', models.ImageField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('ccategory_icon', models.ImageField(blank=True, null=True, upload_to=None)),
                ('subcategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='app.maincategory')),
            ],
        ),
    ]