from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
import uuid

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_app(self, request, provider, config=None):
        # Override the default behavior to be more flexible with SITE_ID
        try:
            return super().get_app(request, provider, config)
        except:
            from allauth.socialaccount.models import SocialApp
            app = SocialApp.objects.filter(provider=provider).first()
            if app:
                return app
            raise

    def pre_social_login(self, request, sociallogin):
        # Automatically connect social accounts to existing users with the same email
        if sociallogin.is_existing:
            return
        
        from django.contrib.auth import get_user_model
        User = get_user_model()
        email = sociallogin.user.email
        if email:
            try:
                user = User.objects.get(email=email)
                sociallogin.connect(request, user)
            except User.DoesNotExist:
                pass

    def populate_user(self, request, sociallogin, data):
        # Ensure a unique username is generated if the default one is taken
        user = super().populate_user(request, sociallogin, data)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # If username is empty or just "Username", try to use email prefix
        if not user.username or user.username.lower() == "username":
            if user.email:
                user.username = user.email.split('@')[0]
            else:
                user.username = "user"

        if User.objects.filter(username=user.username).exists():
            # Append a short unique string to the username if it's taken
            user.username = f"{user.username}_{uuid.uuid4().hex[:4]}"
        
        return user
