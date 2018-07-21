from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/index.html')

def process(request):
    print "processing"
    print request.POST['name']
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    if (not 'count' in request.session):
        request.session['count'] = 1
    else:
        request.session['count'] = request.session['count']+1
    print "resulting"
    context = {
        "name": request.session['name'],
        "location": request.session['location'],
        "language": request.session['language'],
        "comment": request.session['comment'],
        "count": request.session['count'],
    }
    return render(request, 'survey/result.html', context)
