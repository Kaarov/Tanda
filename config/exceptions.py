from typing import Optional

from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.exceptions import NotAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import exception_handler


def drf_exception_handler(exc, context):
    exception_handler(exc, context)

    if isinstance(exc, TandaBaseException):
        return Response(
            {"code": exc.code, "message": exc.message, "field_errors": []},
            status=exc.http_code,
        )

    if isinstance(exc, NotAuthenticated):
        return Response(
            {
                "code": TandaUnauthorized.code,
                "message": TandaUnauthorized.message,
                "error_fields": [],
            },
            status=TandaUnauthorized.http_code,
        )

    if isinstance(exc, AuthenticationFailed):
        return Response(
            {
                "code": TandaAuthenticationFailed.code,
                "message": TandaAuthenticationFailed.message,
                "error_fields": [],
            },
            status=TandaAuthenticationFailed.http_code,
        )

    if isinstance(exc, APIException):
        try:
            return Response(
                {
                    "code": TandaBadRequest.code,
                    "message": TandaBadRequest.message,
                    "field_errors": [
                        {
                            "field": field,
                            "message": message if type(message) is dict else message[0],
                        }
                        for field, message in zip(exc.detail, exc.detail.values())
                    ],
                },
                status=exc.status_code,
            )

        except Exception as e:  # noqa F841
            return Response(
                {
                    "code": TandaBadRequest.code,
                    "message": str(exc),
                    "field_errors": [],
                },
                status=exc.status_code,
            )

    if isinstance(exc, Http404):
        return Response(
            {
                "code": TandaNotFound.code,
                "message": TandaNotFound.message,
                "error_fields": [],
            },
            status=TandaNotFound.http_code,
        )

    return None


class TandaBaseException(Exception):
    code = "UnexpectedException"
    message = "Unexpected error occurred while processing your request"
    http_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    field_errors = []

    def __init__(
        self,
        message: str = "",
        code: str = "",
        http_code: Optional[int] = None,
        field_errors: Optional[list] = None,
    ):
        self.code = code or self.code
        self.message = message or self.message
        self.http_code = http_code or self.http_code
        self.field_errors = field_errors or self.field_errors


class TandaNotFound(TandaBaseException):
    code = "ObjectDoesNotExist"
    message = "Object does not exist"
    http_code = status.HTTP_404_NOT_FOUND


class TandaBadRequest(TandaBaseException):
    code = "BadRequest"
    message = "Invalid request, please try again later"
    http_code = status.HTTP_400_BAD_REQUEST


class TandaPermissionDenied(TandaBaseException):
    code = "PermissionDenied"
    message = "Permission Denied"
    http_code = status.HTTP_403_FORBIDDEN


class TandaUnauthorized(TandaBaseException):
    code = "Unauthorized"
    message = "Unauthorized"
    http_code = status.HTTP_401_UNAUTHORIZED


class TandaAuthenticationFailed(TandaUnauthorized):
    code = "AuthenticationError"
    message = "Authentication Error"
    http_code = status.HTTP_401_UNAUTHORIZED
