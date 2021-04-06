from typing import Dict

from django.core.exceptions import ValidationError

from users.models import User
from users.utils import user_to_dict


def create_account(data: Dict):
    """
    Creates a user object using the dict argument
    """
    try:
        user = User(email=data["email"])
        user.set_password(data["password"])

        user.full_clean()

    except ValidationError as e:
        return {"error": e.message_dict}

    else:
        user.save()
        return user_to_dict(user)
