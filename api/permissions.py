from rest_framework import permissions


# Defining custom permission then add it to the view
class DataCapturerPermission(permissions.DjangoModelPermissions):
  perms_map = {
    'GET': ['%(app_label)s.view_%(model_name)s'],
    'OPTIONS': [],
    'HEAD': [],
    'POST': ['%(app_label)s.add_%(model_name)s'],
    'PUT': ['%(app_label)s.change_%(model_name)s'],
    'PATCH': ['%(app_label)s.change_%(model_name)s'],
    'DELETE': ['%(app_label)s.delete_%(model_name)s'],
  }

  # def has_permission(self, request, view):
  #   user = request.user
  #   if user.is_data_capturer:
  #     return True
  #   print(user.get_all_permissions())
  #   return False
