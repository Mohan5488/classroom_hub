# Generated by Django 4.2.19 on 2025-02-26 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("fname", models.CharField(max_length=50)),
                ("username", models.CharField(max_length=10, unique=True)),
                ("password", models.CharField(max_length=50)),
                ("year", models.IntegerField()),
                ("department", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="StudentLogin",
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
                ("last_login", models.DateTimeField(auto_now_add=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.student"
                    ),
                ),
            ],
        ),
    ]
