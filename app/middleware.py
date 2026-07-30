from django.shortcuts import redirect

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip for login, signup, and static files
        if request.path.startswith('/login/') or request.path.startswith('/signup/') or request.path.startswith('/static/'):
            return self.get_response(request)
            
        # Check session
        if not request.session.get('user_id'):
            return redirect(f'/login/?next={request.path}')
            
        return self.get_response(request)