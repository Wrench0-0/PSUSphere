from django.contrib import admin
from django.urls import path
from studentorg.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
