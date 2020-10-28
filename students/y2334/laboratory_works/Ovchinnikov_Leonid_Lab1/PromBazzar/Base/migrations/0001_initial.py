# Generated by Django 3.1.1 on 2020-09-13 16:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_brok', models.CharField(max_length=100)),
                ('Birthday', models.DateField()),
                ('phone_brok', models.CharField(blank=True, max_length=11)),
                ('address_brok', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_deal', models.CharField(default='0', max_length=4)),
                ('date_deal', models.DateField()),
                ('col_sold', models.IntegerField()),
                ('view_prod', models.CharField(choices=[('N', 'New'), ('U', 'Unon'), ('B', 'Bad')], default='U', max_length=1)),
                ('br_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.broker')),
            ],
        ),
        migrations.CreateModel(
            name='InDeals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_deal', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_prod', models.CharField(max_length=100)),
                ('exp_date', models.DateField()),
                ('about_prod', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_prov', models.CharField(max_length=100)),
                ('address_prov', models.CharField(blank=True, max_length=100)),
                ('date_auth', models.DateField()),
                ('prov_about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('purchases', models.ManyToManyField(to='Base.InDeals')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_supp', models.CharField(default='0', max_length=4)),
                ('price_sold', models.IntegerField()),
                ('date_supp', models.DateField()),
                ('col_supp', models.IntegerField()),
                ('prod_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.product')),
                ('prov_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.provider')),
            ],
        ),
        migrations.AddField(
            model_name='indeals',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='indeals',
            name='deals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.deals'),
        ),
        migrations.AddField(
            model_name='deals',
            name='prod_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.product'),
        ),
    ]