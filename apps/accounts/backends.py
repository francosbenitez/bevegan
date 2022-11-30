# from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password 
from django.contrib.auth.backends import BaseBackend
from apps.accounts.models import Account

class CaseInsensitiveModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # UserModel = get_user_model()
        try:
            # Try to find a user matching your username
            user = Account.objects.get(username=username)

            #  Check the password is the reverse of the username
            if check_password(password, user.password):
                # Yes? return the Django user object
                return user
            else:
                # No? return None - triggers default login failed
                return None
        except Account.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None
        # print('user es', email)
        # if email is None:
        #     email = kwargs.get(UserModel.USERNAME_FIELD)
        # try:
        #     user = UserModel.objects.get(email=email)
        #     # case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
        #     # user = UserModel._default_manager.get(**{case_insensitive_username_field: username})
        # except UserModel.DoesNotExist:
        #     # Run the default password hasher once to reduce the timing
        #     # difference between an existing and a non-existing user (#20760).
        #     # UserModel().set_password(password)
        #     print('usuario no existe')
        # else:
        #     if user.check_password(password):
        #         print(f'el usuario es {user} y esta {user.check_password(password)} ')
        #         return user