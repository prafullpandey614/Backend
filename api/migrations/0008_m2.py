# Generated by Django 4.1.7 on 2023-03-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_thirdone"),
    ]

    operations = [
        migrations.CreateModel(
            name="M2",
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
                ("name", models.CharField(max_length=19)),
            ],
        ),
    ]
