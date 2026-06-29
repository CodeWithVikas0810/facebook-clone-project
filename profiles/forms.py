from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Profile


class EditProfileForm(ModelForm):
    """Update user profile information safely"""

    class Meta:
        model = Profile
        fields = ["bio", "profile_picture", "cover_picture"]

    def clean_profile_picture(self):
        file = self.cleaned_data.get("profile_picture")

        if file:
            if file.size > 2 * 1024 * 1024:
                raise ValidationError("Image too large (max 2MB)")

            valid_types = ["image/jpeg", "image/png", "image/jpg"]
            if hasattr(file, "content_type") and file.content_type not in valid_types:
                raise ValidationError("Only JPG and PNG images are allowed")

        return file

    def clean_cover_picture(self):
        file = self.cleaned_data.get("cover_picture")

        if file:
            if file.size > 2 * 1024 * 1024:
                raise ValidationError("Image too large (max 2MB)")

            valid_types = ["image/jpeg", "image/png", "image/jpg"]
            if hasattr(file, "content_type") and file.content_type not in valid_types:
                raise ValidationError("Only JPG and PNG images are allowed")

        return file
