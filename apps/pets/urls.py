from django.conf.urls import url, include
from apps.pets import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pets'

animal_patterns = [
    url(r'^inicio/$', views.pet_list, name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.pet_detail, name='pet-detail'),
    url(r'^crear/$', views.pet_create, name='pet-create'),
    url(r'^(?P<pk>[0-9]+)/editar/$', views.pet_update, name='pet-edit'),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.pet_delete, name='pet-delete'),
]

urlpatterns = [
    url(r'^$', views.log_in, name='log-in'),
    url(r'^log-out/$', views.log_out, name='log-out'),
    url(r'^tipos/$', views.animal_type_list, name='animal-type-list'),
    url(r'^mascotas/', include(animal_patterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
