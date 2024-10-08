# Generated by Django 5.1.1 on 2024-10-03 00:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("first_name", models.CharField(max_length=60)),
                ("last_name", models.CharField(max_length=60)),
                ("username", models.CharField(max_length=60, unique=True)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("phone_numbre", models.CharField(max_length=50)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("last_loguin", models.DateTimeField(auto_now_add=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                ("is_superadmin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
