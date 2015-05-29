from django.conf.urls import patterns, url

from core.views import RadiostationDetailView

urlpatterns = patterns('core.views',
    url(r'^radiostation/(?P<pk>\d+)/$',
        RadiostationDetailView.as_view(), name='radiostation_detail')
)