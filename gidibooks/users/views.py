import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from users.services import create_account
from users.utils import user_to_dict


@csrf_exempt
def register(request):
    """
    Handles POST request only.

    Converts payload data [json] to dictionary object.

    Uses `create_account` service to create a user account.

    Returns users data as JSON
    """
    payload = json.loads(request.body.decode("utf-8"))

    response = create_account(payload)

    if "error" in response.keys():
        return JsonResponse({"data": response}, status=300)
    return JsonResponse({"data": response}, status=200)


@csrf_exempt
def login_user(request):
    """
    Handles POST request only.

    Converts payload data [json] to dictionary object.

    Uses `authenticate` to verify users email and password

    Returns users data as JSON
    """

    payload = json.loads(request.body.decode("utf-8"))

    user = authenticate(
        email=payload["email"], password=payload["password"]
    )
    user_dict = user_to_dict(user)

    if (
        user is not None
        and user.is_authenticated
        and "success" in user_dict.keys()
    ):
        return JsonResponse({"data": user_dict})
    else:

        return JsonResponse(
            {"data": user_dict},
            status=401,
        )
