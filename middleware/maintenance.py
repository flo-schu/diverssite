import os
from django.conf import settings
from django.http import HttpResponseServerError


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if maintenance mode is enabled
        if maintenance_mode_is_enabled():
            return HttpResponseServerError("Site is temporarily unavailable for maintenance. Please check back later.")

        # Allow request to proceed as normal
        response = self.get_response(request)
        return response


def maintenance_mode_is_enabled():
    return settings.MAINTENANCE_MODE == "on"
