from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.utils.deprecation import MiddlewareMixin
from importlib import import_module

class SeparateSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/admin/'):
            engine = import_module(settings.ADMIN_SESSION_ENGINE)
            session_key = request.COOKIES.get(settings.ADMIN_SESSION_COOKIE_NAME, None)
            request.session = engine.SessionStore(session_key)
        else:
            engine = import_module(settings.FRONTEND_SESSION_ENGINE)
            session_key = request.COOKIES.get(settings.FRONTEND_SESSION_COOKIE_NAME, None)
            request.session = engine.SessionStore(session_key)

    def process_response(self, request, response):
        if request.path.startswith('/admin/'):
            response.set_cookie(settings.ADMIN_SESSION_COOKIE_NAME, request.session.session_key)
        else:
            response.set_cookie(settings.FRONTEND_SESSION_COOKIE_NAME, request.session.session_key)
        return response