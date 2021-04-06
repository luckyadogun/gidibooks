import json

from django.http import JsonResponse
from django.views.decorators import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from users.serices import create_account


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

    if user is not None:
        login(request, user)

        return JsonResponse({"data": user})
    else:
        return JsonResponse(
            {
                "data": "User with that account does not exist"
            },
            status=401,
        )
