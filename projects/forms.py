from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateTimeInput, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.utils import timezone

from projects.models import Worker, Task


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name",
                                                 "last_name",
                                                 "position",)


class WorkerUpdateForm(ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name",
                                                 "last_name",
                                                 "position",)


class TaskCreateForm(ModelForm):
    workers = ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ["name", "description", "deadline", "is_completed",
                  "priority", "task_type", "project", "workers"]
        widgets = {
            "deadline": DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def clean_deadline(self):
        return validate_deadline(self.cleaned_data["deadline"])


class TaskUpdateForm(ModelForm):
    workers = ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ["name", "description", "deadline", "is_completed",
                  "priority", "task_type", "project", "workers"]
        widgets = {
            "deadline": DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def clean_deadline(self):
        return validate_deadline(self.cleaned_data["deadline"])


def validate_deadline(deadline):
    if deadline < timezone.now():
        raise ValidationError("The deadline must be a future date.")
    return deadline
