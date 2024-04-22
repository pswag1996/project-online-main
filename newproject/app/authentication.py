from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import teacher, student

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        try:
            user = teacher.objects.get(username=username)
        except teacher.DoesNotExist:
            try:
                user = student.objects.get(username=username)
            except student.DoesNotExist:
                return None
        if user and check_password(password, user.password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return teacher.objects.get(pk=user_id)
        except teacher.DoesNotExist:
            try:
                return student.objects.get(pk=user_id)
            except student.DoesNotExist:
                return None
