import logging
from django.http import HttpResponse, JsonResponse
from rest_framework.exceptions import APIException

logger = logging.getLogger('molepay')

import logging

# class CustomExceptionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         try:
#             response = self.get_response(request)
#         except Exception as e:
#             logging.error('Uncaught Exception: %s', str(e), exc_info=True)
#             # Handle the error gracefully or return a custom response
#             response = HttpResponse("An unexpected error occurred.", status=500)
#         return response


class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except APIException as e:
            # logger.error(f"API Exception: {str(e)}")
            return JsonResponse({"detail": e.detail}, status=e.status_code)
        except Exception as e:
            logger.exception("Unhandled Exception")
            return JsonResponse({"error": "Internal Server Error"}, status=500)
        return response
