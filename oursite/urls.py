"""oursite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='pages/homepage.html'), name="homepage"),
    url(r'^talk/$', TemplateView.as_view(template_name='pages/talk_homepage.html'), name="talk_homepage"),
    url(r'^resources/$', TemplateView.as_view(template_name='pages/resources.html'), name="resources"),
    url(r'^books$', TemplateView.as_view(template_name='pages/Resources/Books/books.html'), name="books"),
    url(r'^movies-tv$', TemplateView.as_view(template_name='pages/Resources/MoviesTV/moviestv.html'), name="movies-tv"),
    url(r'^websites$', TemplateView.as_view(template_name='pages/Resources/Website/website.html'), name="websites"),
    url(r'^culturalappropriation/$', TemplateView.as_view(template_name='pages/culturalappropriation.html'), name="culturalappropriation"),

    url(r'^cultural-appropriation-survey$', TemplateView.as_view(template_name='pages/Resources/survey/survey.html'), name="survey"),

#    url(r'^posts/cultural-appropriation$', TemplateView.as_view(template_name='pages/homepage.html'), name="homepage"),
#    url(r'^posts/model-minority-myth$', TemplateView.as_view(template_name='pages/homepage.html'), name="homepage"),
#    url(r'^posts/reverse-racism$', TemplateView.as_view(template_name='pages/homepage.html'), name="homepage"),
#    url(r'^posts/vent$', TemplateView.as_view(template_name='pages/vent_homepage.html'), name="homepage"),
#    url(r'^posts/new-vent$', TemplateView.as_view(template_name='pages/vent_homepage.html'), name="post_new_vent"),
#    url(r'^posts/model-minority-myth$', TemplateView.as_view(template_name='pages/homepage.html'), name="homepage"),
]
