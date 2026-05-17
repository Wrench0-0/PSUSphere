from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_app(self, request, provider, config=None):
        # Override the default behavior to be more flexible with SITE_ID
        # If the app isn't found for the current site, try to find any app for the provider
        try:
            return super().get_app(request, provider, config)
        except:
            from allauth.socialaccount.models import SocialApp
            app = SocialApp.objects.filter(provider=provider).first()
            if app:
                return app
            raise
