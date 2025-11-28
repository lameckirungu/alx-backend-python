import logging
from datetime import datetime
from django.http import JsonResponse

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
    

RATE_LIMIT_STORE = {}
MAX_MESSAGES = 5
TIME_WINDOW = 60  # seconds

"""
    Middleware to limit number of chat messages a user can send
    within a certain timeframe, based on their IP address.
"""

class OffensiveLanguageMiddleware: # Misleading name
    """
     Tracks number of requests from an IP address and limits access if threshold exceeded.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):

        if request.method == 'POST' AND request.path.startswith('/chats/send_message/'):
            ip = self.get_client_ip(request)
            now = datetime.now()
            
            # Get or Initialize timestamps for this IP
            if ip not in RATE_LIMIT_STORE:
                RATE_LIMIT_STORE[ip] = []
            timestamps = RATE_LIMIT_STORE[ip]

            # Remove timestamps older than 1 minute
            timestamps = [t for t in timestamps if (now -t) < TIME_WINDOW]
            RATE_LIMIT_STORE[ip] = timestamps

            if len(timestamps) >= MAX_MESSAGES:
                return JsonResponse({
                    'error': 'Rate limit exceeded. Maximum 5 messages per minute allowed.'
                }, status=429)
            timestamps.append(now)

        response = self.get_response(request)
        return response
    
    def get_client_ip(self, request):
        """
        Get Real IP behind Proxy if any
        """

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR', 'unknown')
        return ip
