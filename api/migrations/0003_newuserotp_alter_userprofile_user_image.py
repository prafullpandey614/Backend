# Generated by Django 4.1.7 on 2023-03-03 08:18

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_remove_userprofile_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewUserOTP",
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
                (
                    "email_mobile",
                    models.CharField(
                        default="",
                        max_length=255,
                        unique=True,
                        validators=[api.validators.validate_email_mobile],
                    ),
                ),
                ("otp", models.IntegerField(default=1)),
                ("created_on", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="user_image",
            field=models.ImageField(default="", upload_to="images"),
        ),
    ]
