# Generated by Django 4.1.7 on 2023-03-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_firstone"),
    ]

    operations = [
        migrations.CreateModel(
            name="SecondOne",
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
