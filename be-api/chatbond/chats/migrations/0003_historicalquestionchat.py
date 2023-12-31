# Generated by Django 3.2 on 2023-05-12 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chats", "0002_alter_questionchat_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalQuestionChat",
            fields=[
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("updated_at", models.DateTimeField(blank=True, editable=False)),
                (
                    "id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("content", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("published", "Published"),
                            ("draft", "Draft"),
                            ("pending", "Pending"),
                            ("deleted", "Deleted"),
                        ],
                        default="draft",
                        max_length=10,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="chats.interlocutor",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "question_thread",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="chats.questionthread",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical question chat",
                "verbose_name_plural": "historical question chats",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
