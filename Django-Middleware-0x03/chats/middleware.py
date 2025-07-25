from datetime import datetime, time, timedelta
import logging
import os
from django.http import HttpResponseForbidden

from collections import defaultdict

# Ensure the logs directory or file exists
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, 'requests.log')

# Set up basic file logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(message)s'
)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        path = request.path
        log_entry = f"{datetime.now()} - User: {user} - Path: {path}"
        logging.info(log_entry)

        response = self.get_response(request)
        return response


# === Restrict Access By Time Middleware ===
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Access allowed only from 6PM to 9PM (18:00 to 21:00)
        self.allowed_start = time(18, 0)
        self.allowed_end = time(21, 0)

    def __call__(self, request):
        current_time = datetime.now().time()
        if not (self.allowed_start <= current_time <= self.allowed_end):
            return HttpResponseForbidden("Access to chats is only allowed between 6PM and 9PM.")
        return self.get_response(request)


# === Offensive Language / Rate-Limit Middleware ===
class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Structure: {ip: [timestamps]}
        self.ip_message_log = defaultdict(list)
        self.time_window = timedelta(minutes=1)
        self.message_limit = 5

    def __call__(self, request):
        # Only monitor POST requests
        if request.method == 'POST':
            ip = self.get_client_ip(request)
            now = datetime.now()

            # Clean up old timestamps
            self.ip_message_log[ip] = [
                t for t in self.ip_message_log[ip]
                if now - t <= self.time_window
            ]

            if len(self.ip_message_log[ip]) >= self.message_limit:
                return HttpResponseForbidden("Rate limit exceeded: Max 5 messages per minute.")

            self.ip_message_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        """Get real IP even if behind proxy."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR', '')
