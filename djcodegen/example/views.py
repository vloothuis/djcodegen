from django.views import generic
from . import models


def generate_views(info):
    name = info['name']
    fields = {'model': getattr(models, name)}
    views = []
    for view_class in ('CreateView', 'UpdateView', 'ListView'):
        views.append(type(name + view_class, (getattr(generic, view_class),), fields))
    return views


for topic in models.QUIZ:
    for view in generate_views(topic):
        locals()[view.__name__] = view


