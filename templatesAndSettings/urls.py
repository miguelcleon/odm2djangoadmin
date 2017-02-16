from ajax_select import urls as ajax_select_urls
from django.core.management import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.conf.urls.static import static

# from ODM2CZOData import views # How can I use config file for this??
import importlib

views = importlib.import_module("{}.views".format(settings.APP_NAME))

admin.autodiscover()
admin.site.site_header = settings.SITE_HEADER
admin.site.site_title = settings.SITE_TITLE

# admin_site.admin_view()
urlpatterns = [url(r'^' + settings.URL_PATH + '', include(admin.site.urls)),
               url(r'^' + settings.URL_PATH + 'lookups/', include(ajax_select_urls)),
               url(r'^$', lambda r: HttpResponseRedirect(settings.URL_PATH + '{}/'.format(settings.APP_NAME))),
               url(r'^' + settings.URL_PATH + 'AddSensor.html', views.AddSensor, name="AddSensor"),
               url(r'^' + settings.URL_PATH + 'chartIndex.html', views.chartIndex,
                   name="chartIndex"),
               url(r'^' + settings.URL_PATH + 'AddProfile.html', views.AddProfile,
                   name="AddProfile"),
               url(r'^' + settings.URL_PATH + 'RecordAction.html', views.RecordAction,
                   name="RecordAction"),
               url(r'^' + settings.URL_PATH + 'ManageCitations.html', views.ManageCitations,
                   name="ManageCitations"),
               url(r'^' + settings.URL_PATH + 'chart.html', views.TimeSeriesGraphing,
                   name="TimeSeriesGraphing"),
               url(r'^' + settings.URL_PATH + 'mapdata.html/dataset=(?P<dataset>(\d+))/$',
                   views.web_map, name="WebMap"),
               url(r'^' + settings.URL_PATH + 'mapdata.html', views.web_map, name="WebMap"),
               #  url(r'^' + settings.URL_PATH +'^login/$', login, {'template_name': 'login.html'}),
               url(r'^' + settings.URL_PATH + 'graph/$', views.TimeSeriesGraphing),
               url(r'^' + settings.URL_PATH + 'graph/featureaction=(?P<feature_action>(\d+))/$',
                   views.TimeSeriesGraphing, name="TimeSeriesGraphing"),
               # (?:featureaction-(?P<featureaction>\d+)/)?$  (?P<variable_a>(\d+)
               # (?P<feature_action>(\d+))
               url(r'^' + settings.URL_PATH + 'emaildata/$', views.email_data_from_graph),
               url(r'^' + settings.URL_PATH + 'addannotation/$', views.add_annotation),
               url(r'^' + settings.URL_PATH + 'addL1timeseries/$', views.addL1timeseries),
               url(r'^' + settings.URL_PATH + 'graphfa/featureaction=(?P<feature_action>(\d+))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/featureaction=(?P<feature_action>(\d+))/'
                                     'startdate=(?P<startdate>(\d{4}-\d{2}-\d{2}))/'
                                     'enddate=(?P<enddate>(\d{4}-\d{2}-\d{2}))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/featureaction=(?P<feature_action>(\d+))/'
                                     'resultidu=(?P<resultidu>(\d+))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/featureaction=(?P<feature_action>(\d+))/'
                                     'resultidu=(?P<resultidu>(\d+))/'
                                     'startdate=(?P<startdate>(\d{4}-\d{2}-\d{2}))/'
                                     'enddate=(?P<enddate>(\d{4}-\d{2}-\d{2}))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(r'^' + settings.URL_PATH + 'graph/samplingfeature=(?P<samplingfeature>(\d+))/$',
                   views.TimeSeriesGraphing, name="TimeSeriesGraphing"),
               # (?:featureaction-(?P<featureaction>\d+)/)?$  (?P<variable_a>(\d+)
               # (?P<feature_action>(\d+))
               url(r'^' + settings.URL_PATH + 'graphfa/samplingfeature=(?P<samplingfeature>(\d+))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/samplingfeature=(?P<samplingfeature>(\d+))/'
                                     'startdate=(?P<startdate>(\d{4}-\d{2}-\d{2}))/'
                                     'enddate=(?P<enddate>(\d{4}-\d{2}-\d{2}))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/samplingfeature=(?P<samplingfeature>(\d+))/'
                                     'resultidu=(?P<resultidu>(\d+))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/samplingfeature=(?P<samplingfeature>(\d+))/'
                                     'resultidu=(?P<resultidu>(\d+))/'
                                     'startdate=(?P<startdate>(\d{4}-\d{2}-\d{2}))/'
                                     'enddate=(?P<enddate>(\d{4}-\d{2}-\d{2}))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),

               url(r'^' + settings.URL_PATH + 'mappopup/featureaction=(?P<feature_action>(\d+))/$',
                   views.mappopuploader,
                   name="mappopuploader"),
               url(
                   r'^' + settings.URL_PATH + 'mappopup/samplingfeature=(?P<samplingfeature>(\d+))/'
                                     'popup=(?P<popup>(([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])))/$',
                   views.mappopuploader, name="mappopuploader"),

               url(
                   r'^' + settings.URL_PATH + 'graphfa/samplingfeature=(?P<samplingfeature>(\d+))/'
                                     'popup=(?P<popup>(([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/samplingfeature=(?P<samplingfeature>(\d+))/'
                                     'startdate=(?P<startdate>(\d{4}-\d{2}-\d{2}))/'
                                     'enddate=(?P<enddate>(\d{4}-\d{2}-\d{2}))/'
                                     'popup=(?P<popup>(([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/samplingfeature=(?P<samplingfeature>(\d+))/'
                                     'resultidu=(?P<resultidu>(\d+))/'
                                     'popup=(?P<popup>(([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/samplingfeature=(?P<samplingfeature>(\d+))/'
                                     'resultidu=(?P<resultidu>(\d+))/'
                                     'startdate=(?P<startdate>(\d{4}-\d{2}-\d{2}))/'
                                     'enddate=(?P<enddate>(\d{4}-\d{2}-\d{2}))/'
                                     'popup=(?P<popup>(([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),

               url(r'^' + settings.URL_PATH + 'graphfa/dataset=(?P<dataset>(\d+))/$',
                   views.TimeSeriesGraphingShort,
                   name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/dataset=(?P<dataset>(\d+))/'
                                     'resultidu=(?P<resultidu>(\d+))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/dataset=(?P<dataset>(\d+))/'
                                     'startdate=(?P<startdate>(\d{4}-\d{2}-\d{2}))/'
                                     'enddate=(?P<enddate>(\d{4}-\d{2}-\d{2}))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),
               url(
                   r'^' + settings.URL_PATH + 'graphfa/dataset=(?P<dataset>(\d+))/'
                                     'resultidu=(?P<resultidu>(\d+))/'
                                     'startdate=(?P<startdate>(\d{4}-\d{2}-\d{2}))/'
                                     'enddate=(?P<enddate>(\d{4}-\d{2}-\d{2}))/$',
                   views.TimeSeriesGraphingShort, name="TimeSeriesGraphingShort"),

               url(
                   r'^' + settings.URL_PATH + 'profilegraph/'
                                     'samplingfeature=(?P<samplingfeature>(\d+))/$',
                   views.graph_data, name="graph_data"),
               url(
                   r'^' + settings.URL_PATH + 'profilegraph/'
                                     'samplingfeature=(?P<samplingfeature>(\d+))/'
                                     'popup=(?P<popup>(([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])))/$',
                   views.graph_data, name="graph_data"),
               url(
                   r'^' + settings.URL_PATH + 'profilegraph/'
                                     'selectedrelatedfeature='
                                     '(?P<selectedrelatedfeature>(\d+))/'
                                     'popup=(?P<popup>(([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])))/$',
                   views.graph_data, name="graph_data"),
               url(
                   r'^' + settings.URL_PATH + 'profilegraph/'
                                     'selectedrelatedfeature='
                                     '(?P<selectedrelatedfeature>(\d+))/'
                                     'samplingfeature=(?P<samplingfeature>(\d+))/'
                                     'popup=(?P<popup>(([a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z])))/$',
                   views.graph_data, name="graph_data"),

               # /(?P<startdate>(\d+))/(?P<enddate>(\d+))
               url(r'^' + settings.URL_PATH + 'chartVariableAndFeature.html', views.graph_data,
                   name="graph_data"),
               url(r'^' + settings.URL_PATH + 'soilsscatterplot.html', views.scatter_plot,
                   name="scatter_plot"),
               url(r'^' + settings.URL_PATH + 'publications.html', views.publications,
                   name="publications"),
               # url(r'^' + settings.URL_PATH + 'pubview/citationid=(?P<citationid>(\d+))/$',
               # views.add_pub,
               #    name="add_pub"),
               # url(r'^' + settings.URL_PATH + 'pubview', views.add_pub),
               # for uploaded files like dataloggerfiles
               # url(r'^' + MEDIA_URL +'(?P<path>.*)$', 'django.views.static.serve', {
               #        'document_root': MEDIA_ROOT,
               #    }),
               # url(r'^' + settings.URL_PATH + 'upfiles/(?P<path>.*)$', 'django.views.static.serve',
               #    {'document_root': MEDIA_ROOT}),
               # url(r'^admin/DataloggerfilecolumnsDisplay.html',
               # views.dataloggercolumnView,
               # name="dataloggercolumnView"),

               # url(r'^contas_pagar/pagamento/(?P<id_parcela>\d+)/$',
               # 'contas_pagar.views.retorna_pagamentos_parcela')
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
