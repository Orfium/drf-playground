# Generated by Django 3.1.3 on 2021-09-10 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0003_auto_20210910_1505"),
    ]

    operations = [
        migrations.AddField(
            model_name="details",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="file_owner",
                to="files.user",
            ),
        ),
    ]
