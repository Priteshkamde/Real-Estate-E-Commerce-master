from django.conf.urls import url
from . import views

app_name = 'ecommerce'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^property_details/(?P<pk>[0-9]+)$', views.property_detail, name='property_details'),
    url(r'^post/$', views.post_property, name='post_property'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^register/$', views.register_user, name='register_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]



