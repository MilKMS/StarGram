"""fastgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
# from django.views.static import serve

from contents.views import HomeView, RelationView 

class NonUserTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect('contents_home')
        return super(NonUserTemplateView, self).dispatch(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='contents_home'), 
    path('login/', NonUserTemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', NonUserTemplateView.as_view(template_name='register.html'), name='register'),
    # path('relation/', RelationView.as_view(), name='contents_relation'),
    path('apis/', include('apis.urls')),
    # path('video/', include('video.urls')),
    # url(r'^video/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    # url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)