# Generated by Django 4.2 on 2023-12-03 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='name_book')),
                ('photo_book', models.ImageField(blank=True, null=True, upload_to='phot_book/%y-%m-%d')),
                ('photo_author', models.ImageField(blank=True, null=True, upload_to='photo_author/%y-%m-%d')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('price_rental', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('period_rental', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('solid', 'solid'), ('rental', 'rental'), ('avirable', 'avirable')], max_length=25)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_category', to='pages.category')),
            ],
        ),
    ]
