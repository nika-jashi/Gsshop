# Generated by Django 4.1.4 on 2022-12-26 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_alter_category_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('product_description', models.TextField(max_length=512)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categories.subsubcategory')),
            ],
        ),
    ]
