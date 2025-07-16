from rest_framework_simplejwt.tokens import AccessToken

class CustomAccessToken(AccessToken):
    @property
    def user_id(self):
        return self.payload.get("user_id") or self.payload.get("id") or None
