from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils import timezone

from projects.models import Worker, Task


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name",
                                                 "last_name",
                                                 "position",)


class WorkerUpdateForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name",
                                                 "last_name",
                                                 "position",)


class TaskCreateForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ["name", "description", "deadline", "is_completed",
                  "priority", "task_type", "project", "workers"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def clean_deadline(self):
        return validate_deadline(self.cleaned_data["deadline"])


class TaskUpdateForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ["name", "description", "deadline", "is_completed",
                  "priority", "task_type", "project", "workers"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def clean_deadline(self):
        return validate_deadline(self.cleaned_data["deadline"])


def validate_deadline(deadline):
    if deadline <= timezone.now():
        raise ValidationError("The deadline must be a future date.")
    return deadline


class TaskSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(
                               attrs={
                                   "placeholder": "Search by name"}))


class ProjectSearchForm(forms.Form):
    name = forms.CharField(
        max_length=64,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )
