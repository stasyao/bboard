from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, 
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phone_number, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(email, phone_number, password, **other_fields)
