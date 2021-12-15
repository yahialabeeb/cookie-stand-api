# Generated by Django 4.0 on 2021-12-15 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookieStand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('hourly_sales', models.JSONField(blank=True, default=list)),
                ('minimum_customers_per_hour', models.IntegerField(default=0)),
                ('maximum_customers_per_hour', models.IntegerField(default=0)),
                ('average_cookies_per_sale', models.FloatField(default=0)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]