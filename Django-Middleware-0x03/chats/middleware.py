from datetime import datetime
import logging
import os

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
