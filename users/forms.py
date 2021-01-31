from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'phone_number',
            'last_name',
            'first_name',
            'middle_name',
            'call_reception_time',
        )
