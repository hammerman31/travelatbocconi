from django.utils.deprecation import MiddlewareMixin

class XFrameOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.startswith('/trips/'):
            response['X-Frame-Options'] = 'SAMEORIGIN'
        return response
