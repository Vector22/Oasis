"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# import for statics media files
from django.conf import settings
from django.conf.urls.static import static

import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('social-auth/',
         include('social_django.urls', namespace='social')),
    path('images/', include('images.urls', namespace='images')),
]

# Django serve the media files only in development server
# If ENV_AWS is setted, then serve from amazon s3 bucket
# if settings.DEBUG or os.environ.get('ENV_AWS') == 'PRODUCTION':
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
