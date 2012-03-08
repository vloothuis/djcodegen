from django.conf.urls.defaults import patterns, include, url
from .example.models import QUIZ
from .example import views

URL_PATTERNS = {
    'CreateView': r'{}/create/$',
    'UpdateView': r'{}/(?P<pk>\d+)/$',
    'ListView': r'{}/$',
}

def generate_urls():
    urls = []
    for topic in QUIZ:
        for view_cls in ('CreateView', 'UpdateView', 'ListView'):
            urls.append(url(URL_PATTERNS[view_cls].format(topic['name'].lower()),
                            getattr(views, topic['name'] + view_cls).as_view()))
    return urls

urlpatterns = patterns('',
    *generate_urls()
)
