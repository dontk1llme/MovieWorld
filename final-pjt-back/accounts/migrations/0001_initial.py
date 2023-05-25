# Generated by Django 3.2.13 on 2023-05-25 03:09

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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('followings', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_introduction', models.TextField(blank=True)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=50)),
                ('nick_name', models.CharField(max_length=100)),
                ('img', models.ImageField(default='profilepic.png', upload_to='profile/%Y/%m/%d/')),
                ('feel', models.IntegerField(default=1)),
                ('ytb', models.CharField(default='https://www.youtube.com/embed/zaLJfJ8ESm0', max_length=100)),
                ('action', models.IntegerField(default=0)),
                ('adventure', models.IntegerField(default=0)),
                ('animation', models.IntegerField(default=0)),
                ('comedy', models.IntegerField(default=0)),
                ('crime', models.IntegerField(default=0)),
                ('documentary', models.IntegerField(default=0)),
                ('drama', models.IntegerField(default=0)),
                ('family', models.IntegerField(default=0)),
                ('fantasy', models.IntegerField(default=0)),
                ('history', models.IntegerField(default=0)),
                ('horror', models.IntegerField(default=0)),
                ('music', models.IntegerField(default=0)),
                ('mystery', models.IntegerField(default=0)),
                ('romance', models.IntegerField(default=0)),
                ('science', models.IntegerField(default=0)),
                ('tv', models.IntegerField(default=0)),
                ('thriller', models.IntegerField(default=0)),
                ('war', models.IntegerField(default=0)),
                ('western', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(editable=False, max_length=150)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
