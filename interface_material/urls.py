from django.conf.urls import url

urlpatterns = [
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'admin:login'}, name='logout'),
]
