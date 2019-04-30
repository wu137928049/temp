
from django.conf.urls import patterns

urlpatterns = patterns(
    'gprs.views',
    (r'^1/$', 'gprs'),
    (r'^(\d)/(\w+)/$','xxsj'),
    (r'^gprs/(\w+)/$','bo_d'),
    (r'^xq/$', 'xq'),
    (r'^quanl/(\w+)/(\d)$', 'quanl'),
    (r'^cuoql/(\d)$', 'cuoql'),
    (r'^txzs/(\d)$', 'txzs'),
    (r'^dtxzs/(\d)/(\d)$', 'dtxzs'),
    (r'^cuodtxzs/(\d)/(\d)$', 'cuodtxzs'),

)