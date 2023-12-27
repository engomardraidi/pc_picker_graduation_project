from rest_framework.permissions import IsAuthenticated

class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        refresh_token = request.session.get('refresh_token', None)

        return request.user.is_authenticated and refresh_token != None