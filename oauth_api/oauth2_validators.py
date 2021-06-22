from oauth2_provider.oauth2_validators import OAuth2Validator

class Validator(OAuth2Validator):

    def get_userinfo_claims(self, request):
        claims = super().get_userinfo_claims(request)
        claims["lastname"] = request.user.last_name
        claims["firstname"] = request.user.first_name
        claims["email"] = request.user.email
        return claims