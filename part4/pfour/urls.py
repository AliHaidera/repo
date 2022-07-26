from django.conf.urls import url
from pfour import views
app_name='pfour'

urlpatterns=[
    url(r'^form/$',views.form,name='form'),
    url(r'^other/$',views.other,name='other'),
]
