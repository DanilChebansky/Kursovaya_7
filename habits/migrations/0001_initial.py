# Generated by Django 4.2.2 on 2024-10-02 21:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
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
                    "place",
                    models.CharField(
                        blank=True,
                        help_text="Укажите место выполнения привычки",
                        max_length=255,
                        null=True,
                        verbose_name="Место выполнения привычки",
                    ),
                ),
                (
                    "habit_time",
                    models.TimeField(
                        blank=True,
                        help_text="Укажите время напоминания о выполнении привычки",
                        null=True,
                        verbose_name="Время напоминания о выполнении привычки",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        help_text="Укажите, в чем заключается привычка",
                        max_length=255,
                        verbose_name="Действие",
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False,
                        help_text="Укажите, приятная ли привычка",
                        verbose_name="Признак приятной привычки",
                    ),
                ),
                (
                    "period",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Укажите, раз во сколько дней будет выполняться привычка",
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(7)],
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "award",
                    models.CharField(
                        blank=True,
                        help_text="Укажите, чем будете себя вознаграждать за выполнение",
                        max_length=255,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "action_time",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Укажите время выполнения привычки в секундах",
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(120)],
                        verbose_name="Время на выполнение",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False,
                        help_text="Укажите, доступна ли Ваша привычка, как пример для заполнения другими пользователями",
                        verbose_name="Признак публичности",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="habits",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите связаную привычку",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="related_habits",
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
        ),
    ]
