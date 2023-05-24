from django.urls import path
from . import views as SitemapViews

urlpatterns = [
    path('', SitemapViews.index),
    path('sitemap', SitemapViews.sitemap),
    path('blog', SitemapViews.blog),
    path('about', SitemapViews.about)
]