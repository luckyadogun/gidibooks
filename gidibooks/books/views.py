import json

from django.http import JsonResponse

from books.services import find_book


def search(request):
    """
    Handles GET request only.

    Gets query parameter from the request and converts to a list

    Uses `find_book` service to find a book with items in the list

    Returns book data as JSON
    """

    payload = json.loads(request.body.decode("utf-8"))

    response = find_book(payload)

    if "error" in response.keys():
        return JsonResponse({"data": response}, status=300)
    return JsonResponse({"data": response}, status=200)


def my_books(request):
    """
    Handles GET request only.

    Gets user_id as string

    Uses `my_borrowed_books` to find the users borrowed books

    Returns book data as JSON
    """

    response = my_borrowed_books(payload)

    if "error" in response.keys():
        return JsonResponse({"data": response}, status=300)
    return JsonResponse({"data": response}, status=200)


def borrow(request):
    """
    Handles POST request only.

    Payload is dictionary object container a possible list of book_ids
    and the user_id

    Uses `borrow_book` to request for certain books.
    All requests are pending till the admin approves the request

    Returns book data as JSON
    """

    response = borrow_books(payload)

    if "error" in response.keys():
        return JsonResponse({"data": response}, status=300)
    return JsonResponse({"data": response}, status=200)
