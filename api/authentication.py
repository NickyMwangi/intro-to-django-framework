from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


# Use this to replace Token with Bearer when doing authentication.
class TokenAuthentication(BaseTokenAuth):
  keyword = 'Bearer'
