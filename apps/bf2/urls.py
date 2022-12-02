from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^issuers_count$', views.issuers_count, name='v2_api_issuers_count'),
    url(r'^badgeclasses_count$', views.badgeclasses_count, name='v2_api_badgeclasses_count'),
    url(r'^badgeclasses_count/issuer/(?P<entity_id>[^/]+)$', views.badgeclasses_for_issuer_count, name='v2_api_badgeclasses_for_issuer_count'),
    url(r'^badgeinstances_count/issuer/(?P<entity_id>[^/]+)$', views.badgeinstances_for_issuer_count, name='v2_api_badgeinstances_for_issuer_count'),
    url(r'^badgeinstances_count/badgeclass/(?P<entity_id>[^/]+)$', views.badgeinstances_for_badgeclass_count, name='v2_api_badgeinstances_for_badgeclass_count'),
]
