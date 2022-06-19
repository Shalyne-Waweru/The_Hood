# Generated by Django 4.0.5 on 2022-06-19 21:21

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
            name='NeighbourHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('emergency_number', models.IntegerField()),
                ('police_number', models.IntegerField()),
                ('hood_image', models.ImageField(upload_to='hood-images/')),
                ('occupants', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='occupants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='My Bio', max_length=500)),
                ('profile_pic', models.ImageField(default='default.png', upload_to='profile-images/')),
                ('location', models.CharField(blank=True, default='My Location', max_length=50)),
                ('neighbourhood', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='hood.neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('business_image', models.ImageField(default='default.png', upload_to='business-images/')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood', to='hood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]