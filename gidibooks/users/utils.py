from django.forms.models import model_to_dict

from users.models import User


def user_to_dict(user: User):
    """
    Accepts user object or user email

    Utility object that converts a user object to clean dictionary
    """

    EXCLUDED_FIELDS = [
        "logentry",
        "id",
        "password",
        "last_login",
        "groups",
        "user_permissions",
    ]

    user_obj = None

    try:
        if isinstance(user, User):
            user_obj = user
        else:
            user_obj = User.objects.get(email=user)

    except User.DoesNotExist:
        return {
            "error": "User with that account does not exist"
        }

    else:
        user_dict = model_to_dict(
            user_obj, exclude=EXCLUDED_FIELDS
        )
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["date_joined"] = user_dict[
            "date_joined"
        ].strftime("%Y-%m-%d")

        return {"success": user_dict}
