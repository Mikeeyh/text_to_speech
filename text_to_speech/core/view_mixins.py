from django.core.exceptions import PermissionDenied

#
# class OwnerRequiredMixin:  # more dynamic
#     user_field = "user"
#
#     def get_object(self, queryset=None):  # This does not allow other user to edit the pet
#         obj = super().get_object(queryset=queryset)
#         obj_user = getattr(obj, self.user_field, None)
#         if not self.request.user.is_authenticated \
#                 or obj_user != self.request.user:
#             raise PermissionDenied
#         return obj


from django.contrib.auth import mixins as auth_mixins


class OwnerRequiredMixin(auth_mixins.LoginRequiredMixin):
    user_field = "user"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj_user = getattr(obj, self.user_field, None)
        if obj_user != self.request.user:
            raise PermissionDenied

        return obj
