# -*- coding: utf-8 -*-
from django import template
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.conf import settings
import os, mimetypes, settings

register = template.Library()

# http://djangosnippets.org/snippets/101/
def send_file(path, filename = None, mimetype = None):
    if filename is None: filename = os.path.basename(path)
    if mimetype is None:
        mimetype, encoding = mimetypes.guess_type(filename)
    data = open(path, "rb")
    response = HttpResponse(data, mimetype=mimetype)
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

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
            # download
            #basename, extension = os.path.splitext(pathfull[:-1])
            #if extension:
            #    my_data = os.path.join(settings.ROOT, pathfull[1:-1])
            #    #return send_file(os.path.join(settings.ROOT, pathfull[1:-1]))
            #    response = HttpResponse(my_data, mimetype='application/vnd.ms-excel')
            #    response['Content-Disposition'] = 'attachment; filename=foo.xls'
            #    return response
    return locals()