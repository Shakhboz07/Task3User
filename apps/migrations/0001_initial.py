# Generated by Django 4.1.2 on 2022-10-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("picture", models.ImageField(upload_to="user/")),
                ("title", models.CharField(max_length=255)),
                ("company", models.CharField(max_length=255)),
                ("created_date", models.DateTimeField(auto_now=True)),
                (
                    "time",
                    models.CharField(
                        choices=[
                            ("Full-time", "Full Time"),
                            ("Part-time", "Part Time"),
                        ],
                        default="Full-time",
                        max_length=55,
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        choices=[
                            ("Toronto, CAN", "Toronto"),
                            ("New York, US", "New York"),
                            ("Mumbai, IN", "Mumbai"),
                        ],
                        default="New York, US",
                        max_length=55,
                    ),
                ),
                ("price", models.IntegerField()),
                ("field_name", models.CharField(max_length=255)),
            ],
        ),
    ]