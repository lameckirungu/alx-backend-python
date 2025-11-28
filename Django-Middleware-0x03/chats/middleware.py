import logging
from datetime import datetime

# Configure logger to write to 'requests.log' file
logger = logging.getLogger('request_logger')
if not logger.handlers: # Prevent adding handler to the dev server
    handler = logging.FileHandler('requests.log')
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

class RequestLoggingMiddleware:
    """
    Middleware to log user's request details
    """

    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Get User 
        user = request.user if request.user.is_authenticated else 'Anonymous'

        # Log the request B4 processing
        logger.info(f"{datetime.now()} - User:{user} - Path:{request.path}")

        # Process the request
        response = self.get_response(request)

        return response
    

class RestrictAccessByTimeMiddleware:
    """
    Middleware to restrict access to messaging app during certain hours
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        # Restrict access between 9PM and 6PM
        if 21 <= current_hour or current_hour < 6:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("Access to the messaging app is restricted during this time.")
        response = self.get_response(request)
        return response