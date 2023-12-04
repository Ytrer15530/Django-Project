from .models import UserStat


class UserStatMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        headers = request.headers
        UserStat.objects.create(headers=headers)

        response = self.get_response(request)

        return response
