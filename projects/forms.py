from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from projects.models import Worker


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
