"""audioviz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin

from films  import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('films/', include('films.urls', namespace='films')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls, name='admin'),
    path('boutique/', TemplateView.as_view(template_name='boutique.html'), name='boutique'),
    path('audioviz/', TemplateView.as_view(template_name='audioviz.html'), name='audioviz'),
    path('Blog/', TemplateView.as_view(template_name='audioviz_Blogger.html'), name='audioviz_blogger'),
    path('blog/', include('blog.urls')), 
    path('summernote/', include('django_summernote.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns