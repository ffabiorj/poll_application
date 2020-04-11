from django.forms import ModelForm
from core.models import Poll


class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ["question", "option_one", "option_two", "option_three"]
