from django.urls import path, include
from . import views as SitemapViews

urlpatterns = [
    path('', SitemapViews.sitemap),
]