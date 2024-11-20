from rest_framework.permissions import BasePermission


class CustomerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class BusinessUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.business

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
