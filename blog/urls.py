from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^$', views.post_list, name='post_list'),
    url(r'^cultural-appropriation$', views.post_list_cultural_appropriation, name='post_list_cultural_appropriation'),
    url(r'^model-minority-myth$', views.post_list_mmm, name='post_list_mmm'),
    url(r'^reverse-racism$', views.post_list_rr, name='post_list_rr'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^category$', views.category_list, name='category_list'),
    url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
]
