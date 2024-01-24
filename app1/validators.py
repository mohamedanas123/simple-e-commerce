from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

class CustomPassword(BaseValidator):
    def validate(self,password,user=None):
        if len(password)<8:
            raise ValidationError(
                "Password must be at least 8 characters long."
            )
    def get_help_text(self):
        return "Password must be at least 8 characters long."
