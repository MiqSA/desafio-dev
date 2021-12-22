from app.main.services.standards import Output
from werkzeug.exceptions import HTTPException
import json

class ErrorHandler:
    def __init__(self, app):
        self.app = app

    def handles(self):
        @self.app.errorhandler(HTTPException)
        def handle_exception(error):
            return Output().response_api(error.code, None)
