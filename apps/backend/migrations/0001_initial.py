# Generated by Django 5.1.5 on 2025-04-08 08:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DynamicSchema",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("config", models.JSONField(db_index=True, default=dict)),
                (
                    "expires_in",
                    models.PositiveIntegerField(db_index=True, default=86400),
                ),
                (
                    "csv",
                    models.FileField(
                        blank=True, null=True, upload_to="dynamic_schemas/csv/"
                    ),
                ),
                (
                    "json",
                    models.FileField(
                        blank=True, null=True, upload_to="dynamic_schemas/json/"
                    ),
                ),
                (
                    "xlsx",
                    models.FileField(
                        blank=True, null=True, upload_to="dynamic_schemas/xlsx/"
                    ),
                ),
            ],
            options={
                "verbose_name": "Dynamic Schema",
                "verbose_name_plural": "Dynamic Schemas",
                "db_table": "dynamic_schema",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Gallery",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=255, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("images", models.ImageField(blank=True, null=True, upload_to="")),
            ],
            options={
                "verbose_name": "Gallery",
                "verbose_name_plural": "Galleries",
                "db_table": "gallery",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Type",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=255, unique=True)),
                ("type", models.CharField(db_index=True, max_length=255)),
                ("is_active", models.BooleanField(db_index=True, default=True)),
            ],
            options={
                "verbose_name": "Type",
                "verbose_name_plural": "Types",
                "db_table": "type",
                "ordering": ["name"],
            },
        ),
    ]
