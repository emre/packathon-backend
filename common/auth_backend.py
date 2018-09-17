import json

from steemconnect.client import Client

from django.contrib.auth import get_user_model


class SteemConnectBackend:

    def authenticate(self, **kwargs):
        if 'username' in kwargs:
            return None

        # validate the access token with /me endpoint and get user information
        client = Client(access_token=kwargs.get("access_token"))

        user = client.me()
        if 'name' not in user:
            return None

        user_model = get_user_model()
        metadata = {}
        profile_about, profile_image, profile_location = None, None, None
        if 'json_metadata' in user["account"]:
            metadata = json.loads(user["account"]["json_metadata"])
            profile = metadata.get("profile", {})
            profile_about = profile.get("about")
            profile_image = profile.get("profile_image")
            profile_location = profile.get("location")

        try:
            user = user_model.objects.get(username=user["name"])
        except user_model.DoesNotExist:
            user = user_model.objects.create_user(
                username=user["name"],
                name=user["name"])
        user.profile_about = profile_about
        user.profile_image = profile_image
        user.profile_location = profile_location
        user.save()

        return user

    def get_user(self, user_id):
        user_model = get_user_model()

        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None