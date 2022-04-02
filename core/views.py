from multiprocessing import context
from os import link
from statistics import LinearRegression
from time import process_time
from unicodedata import name
from django.shortcuts import redirect, render, get_object_or_404
from django.http.response import HttpResponse, Http404
from core.models import Link
from django.template import loader
from core.forms import LinkForm, RegisterForm

# Create your views here.

def hello(request):
    # logic goes here
    return HttpResponse("<h1>Salom dunyo!</h1>")

def bye(request):
    # logic goes here
    return HttpResponse("<h1>Ko'rishguncha hayr!</h1>")

def sahifa(request):
    return render(request, "hello.html", {})

# def link_list(request):
#     links = Link.objects.all()
#     _html_template = loader.get_template('link_list.html')
#     context = {
#         'title' : 'Bu havola',
#         'linklar' : links
#     }
#     _html = _html_template.render(context=context, request=request)
#     return HttpResponse(_html)

def link_list(request):
    links = Link.objects.all()
    context = {
        'title' : 'Bu havola',
        'linklar' : links
    }
    return render(request, 'link_list.html', context)

# def link_detail(request, link_id): 
#     try:
#         link = Link.objects.get(id=link_id)
#     except:
#         raise Http404('bunday sahifa mavjud emas')

#     return render(request, 'link_detail.html', {'link':link})


def link_detail(request, link_id): 
    link = get_object_or_404(Link, id=link_id)
    return render(request, 'link_detail.html', {'link':link})

# def link_create(request):
#     errors = {}
#     data = {}

#     print(f"=================={request.method}===================")

#     if request.method == 'GET':
#         print("Bu so'rov GET metodi")
#         print("request.GET=", request.GET)
#         # print("\n\n\n\n", dict(request.GET))
    
#     if request.method == 'POST':
#         # print("Bu so'rov POST metodi")
#         # print("request.POST=", request.POST)
#         # print("\n\n\n\n", dict(request.POST))
#         link_name = request.POST.get('name')
#         link_description = request.POST.get('description')
#         link_url = request.POST.get('url')
#         data['name'] = link_name
#         data['description'] = link_description
#         data['url'] = link_url
#         # new_link = Link(name=link_name, description=link_description, url=link_url)
#         # new_link.name = link_name
#         # new_link.description = link_description
#         # new_link.url = link_url
        
#         if link_name and link_url:
#             old_link = Link.objects.filter(name=link_name)
#             if old_link:
#                 errors['other'] = 'Bunday havola mavjud'
#             new_link = Link.objects.create(
#                 name = link_name,
#                 description = link_description,
#                 url = link_url
#             )
#             return redirect("/havolalar/")
#         else:
#             if not link_name:
#                 errors['name'] = 'iltimos link nomini kiriting'
#             if not link_url:
#                 errors['url'] = 'iltimos url adresni kiriting'

#     # a = request.POST['fname']
#     # b = request.POST.get('lname')
#     # print('ismi:', a, 'familiyas:', b)
    
#     return render(request, 'link_create.html', {'errors':errors, 'data':data})

def link_create(request):

    form = LinkForm()
    errors = {}
    data = {}

    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/havolalar/')

    return render(request, 'link_create.html', {'errors':errors, 'data':data, 'form':form})


def link_update(request, link_id2):
    link = get_object_or_404(Link, id=link_id2)
    form = LinkForm(instance=link)

    if request.method == 'POST':
        form = LinkForm(instance=link, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("/havolalar/")
        
    return render(request, 'link_update.html', {'form':form})

def register_view(request):
    form = RegisterForm()
    print('is_bound', form.is_bound)
    print('fields', form.fields)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print('data', form.data)
        if form.is_valid():
            return redirect('/havolalar/')
        print('cleaned_form', form.cleaned_data)
    return render(request, 'register_view.html', {'form':form})
    