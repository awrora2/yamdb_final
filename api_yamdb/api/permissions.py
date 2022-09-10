from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'admin'

    def has_object_permission(self, request, view, obj):
        if request.method in ('POST', 'PATCH', 'DELETE',):
            return request.user.role == 'admin'
        return True


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated


class IsAdminOrAuthenticatedOrModerator(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method in ('POST', 'PATCH',):
            return request.user.is_authenticated
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_moderator)

    def has_object_permission(self, request, view, obj):
        if request.method in ('PATCH', 'DELETE',):
            return request.user.is_authenticated and (
                obj.author == request.user
                or request.user.is_admin or request.user.is_moderator)
        return True


class IsAuthorOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            and request.user.is_anonymous
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator
        )


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if (request.user.is_authenticated and request.user.is_admin
                and request.method in ['GET', 'POST', 'PATCH', 'DELETE']):
            return True
        return False
