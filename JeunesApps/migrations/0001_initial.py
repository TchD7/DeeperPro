# Generated by Django 3.2.4 on 2021-11-16 13:43

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supports', '0001_initial'),
        ('Eglises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OuviresJeunesPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_de_naissance', models.DateField()),
                ('lieu_de_naissance', models.CharField(max_length=100)),
                ('groupe_sanguin', models.CharField(max_length=25)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('rhesus', models.CharField(max_length=10)),
                ('numero_de_telephone1', models.IntegerField()),
                ('numero_de_telephone2', models.IntegerField()),
                ('talents_de_l_ouvrier', models.CharField(max_length=400)),
                ('avec_qui_vit_il', models.CharField(max_length=100)),
                ('nombre_de_freres', models.IntegerField()),
                ('les_freres_sont_ils_dans_leglise', models.BooleanField()),
                ('nom_des_freres', models.CharField(max_length=500)),
                ('nombre_de_soeurs', models.IntegerField()),
                ('les_soeurs_sont_elles_dans_leglise', models.BooleanField()),
                ('nom_des_soeurs', models.CharField(max_length=500)),
                ('nom_des_parentes', models.CharField(max_length=400)),
                ('les_parents_sont_ils_dans_leglise', models.BooleanField()),
                ('numero_de_telephone_des_parents_ou_tuteurs', models.IntegerField()),
                ('classe_ou_niveau_d_etude', models.CharField(blank=True, max_length=200, null=True)),
                ('Faculte_ou_domaine_d_emploie', models.CharField(blank=True, max_length=200, null=True)),
                ('lieu_de_residence_du_jeune', models.CharField(max_length=300)),
                ('distance_maison_district', models.CharField(max_length=100)),
                ('distance_maison_lieu_de_travail', models.CharField(max_length=100)),
                ('ouvrier_images', models.ImageField(blank=True, null=True, upload_to='images/ouvrier')),
                ('add_date', models.DateField(auto_now_add=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eglises.districts')),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supports.ocupation')),
                ('role_dans_leglise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supports.roles')),
                ('sexe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supports.sexe')),
            ],
        ),
        migrations.CreateModel(
            name='JeunesPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_de_naissance', models.DateField()),
                ('lieu_de_naissance', models.CharField(max_length=100)),
                ('dirigeant', models.CharField(max_length=300)),
                ('groupe_sanguin', models.CharField(max_length=25)),
                ('rhesus', models.CharField(max_length=10)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('numero_de_telephone_du_jeune', models.IntegerField(blank=True, null=True)),
                ('talents_du_jeune', models.CharField(max_length=400)),
                ('avec_qui_vit_il', models.CharField(max_length=100)),
                ('nombre_de_freres', models.IntegerField()),
                ('les_freres_sont_ils_dans_leglise', models.BooleanField()),
                ('nom_des_freres', models.CharField(max_length=500)),
                ('nombre_de_soeurs', models.IntegerField()),
                ('les_soeurs_sont_elles_dans_leglise', models.BooleanField()),
                ('nom_des_soeurs', models.CharField(max_length=500)),
                ('nom_des_parentes', models.CharField(max_length=400)),
                ('les_parents_sont_ils_dans_leglise', models.BooleanField()),
                ('numero_de_telephone_des_parents_ou_tuteurs', models.IntegerField()),
                ('classe_ou_niveau_d_etude', models.CharField(blank=True, max_length=200, null=True)),
                ('Faculte_ou_domaine_d_emploie', models.CharField(blank=True, max_length=200, null=True)),
                ('lieu_de_residence_du_jeune', models.CharField(max_length=300)),
                ('distance_maison_district', models.CharField(max_length=100)),
                ('distance_maison_ecole', models.CharField(max_length=100)),
                ('jeune_images', models.ImageField(blank=True, null=True, upload_to='images/jeunes')),
                ('add_date', models.DateField(auto_now_add=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eglises.districts')),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supports.ocupation')),
                ('role_dans_leglise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supports.roles')),
                ('sexe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supports.sexe')),
            ],
        ),
    ]