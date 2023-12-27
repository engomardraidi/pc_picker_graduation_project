from rest_framework import permissions

class IsSuperAdmin(permissions.IsAdminUser):
    def has_permission(self, request, view):
        refresh_token = request.session.get('refresh_token', None)

        return request.user.is_superuser and refresh_token != None