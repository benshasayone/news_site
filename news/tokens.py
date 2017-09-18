from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, obj, timestamp):
        return (
            six.text_type(obj.pk) + six.text_type(timestamp) +
            six.text_type(obj.status)
        )


account_activation_token = TokenGenerator()
