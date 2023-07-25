from rest_framework import permissions

from api.permissions import DataCapturerPermission


# global definition of permission
class DataCapturerPermissionMixins:
  permission_classes = [permissions.IsAuthenticated, DataCapturerPermission]
