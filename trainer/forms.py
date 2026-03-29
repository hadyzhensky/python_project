"""Forms for SQL Trainer application."""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Form for user registration."""

    class Meta:
        """Meta options for SignUpForm."""

        model = User
        fields = ("username", "password1", "password2")
