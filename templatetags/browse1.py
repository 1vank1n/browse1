# -*- coding: utf-8 -*-
from django import template
from django.http import HttpResponse
from django.conf import settings
import os

register = template.Library()

@register.inclusion_tag('browse1.html', takes_context = True)
def browse1(context, path):
    request = context['request']
    path = request.META['PATH_INFO']
    for root, dirs, files in os.walk('.' + path, topdown=False):
        pass
    
    # breadcrumbs
    breadcrumbs = []
    pathfull = '/'
    for b in path.split('/'):
        if b:
            pathfull += b + '/' 
            b = {'name': b, 'url': pathfull}
            breadcrumbs.append(b)
    return locals()