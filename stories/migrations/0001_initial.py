# Generated by Django 2.2.7 on 2019-11-17 11:56

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
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
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_case', models.CharField(blank=True, help_text='Make your title attention-grabbing and informative.', max_length=255, null=True, verbose_name='Your case name ')),
                ('produit', models.CharField(help_text='help text...', max_length=125, null=True, verbose_name='Le produit ')),
                ('image_produit', models.ImageField(blank=True, help_text='help text...', null=True, upload_to='images/', verbose_name='Figure associée au produit')),
                ('date', models.CharField(help_text='help text...', max_length=125, null=True, verbose_name='Date')),
                ('context', djrichtextfield.models.RichTextField(help_text='Son histoire, le contexte...', null=True, verbose_name='Context')),
                ('context_images', models.ImageField(blank=True, help_text='help text...', null=True, upload_to='images/', verbose_name='Figure associée au contexte')),
                ('description', djrichtextfield.models.RichTextField(help_text='help text...', null=True, verbose_name='Description du produit')),
                ('description_shema', models.ImageField(blank=True, help_text='help text...', null=True, upload_to='images/', verbose_name='Figure associée à la description')),
                ('diagnostic', djrichtextfield.models.RichTextField(help_text='help text...', null=True, verbose_name='Diagnostic de la nouveauté')),
                ('diagnostic_shema', models.ImageField(blank=True, help_text='help text...', null=True, upload_to='images/', verbose_name='Figure associée à la diagnostic de la nouveauté')),
                ('processus', djrichtextfield.models.RichTextField(blank=True, help_text='help text...', null=True, verbose_name='Description du processus d’innovation')),
                ('processus_shema', models.ImageField(blank=True, help_text='help text...', null=True, upload_to='images/', verbose_name='Figure associée à la description du processus d’innovation')),
                ('reference', djrichtextfield.models.RichTextField(help_text='help text...', null=True, verbose_name='Références')),
                ('abstract', djrichtextfield.models.RichTextField(help_text='help text...', null=True, verbose_name='Abstract')),
                ('auteur', models.CharField(help_text='help text...', max_length=200, null=True, verbose_name="L(es)'auteur(s)")),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, help_text='help text...', verbose_name='date de création')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, help_text='help text...', verbose_name='date de publication')),
            ],
        ),
        migrations.CreateModel(
            name='Mois',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(default='#007bff', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_school', models.CharField(max_length=30, unique=True)),
                ('adresse_school', models.CharField(max_length=90)),
                ('speciality_school', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('premier_stop', models.TextField(blank=True, max_length=200, null=True)),
                ('deuxieme_stop', models.TextField(blank=True, max_length=200, null=True)),
                ('limit_stop', models.TextField(blank=True, max_length=200, null=True)),
                ('date_premier_stop', models.DateTimeField(blank=True, null=True)),
                ('date_deuxieme_stop', models.DateTimeField(blank=True, null=True)),
                ('date_limit_stop', models.DateTimeField(blank=True, null=True)),
                ('color', models.CharField(default='#007bff', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(default='#007bff', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(default='#007bff', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('date_evaluation', models.DateTimeField(default=django.utils.timezone.now)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_evaluation', to='stories.Cases')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert', to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases_state', to='stories.State')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Comment')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='stories.Cases')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cases',
            name='mois',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases_mois', to='stories.Mois'),
        ),
        migrations.AddField(
            model_name='cases',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cases',
            name='school_case',
            field=models.ForeignKey(help_text='Add help text(School)...', on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='stories.School', verbose_name='Sélectionnez votre Etablissement'),
        ),
        migrations.AddField(
            model_name='cases',
            name='subject',
            field=models.ForeignKey(help_text='hLe domaine...', on_delete=django.db.models.deletion.CASCADE, related_name='cases_subject', to='stories.Subject', verbose_name='Subject'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('first', models.CharField(blank=True, max_length=25)),
                ('last', models.CharField(blank=True, max_length=25)),
                ('school', models.ManyToManyField(related_name='teachers_schools', to='stories.School')),
                ('studies', models.ManyToManyField(related_name='teacher_studies', to='stories.Cases')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('first', models.CharField(blank=True, max_length=25)),
                ('last', models.CharField(blank=True, max_length=25)),
                ('school', models.ManyToManyField(related_name='students_school', to='stories.School')),
            ],
        ),
    ]
