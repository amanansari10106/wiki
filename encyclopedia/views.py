from django.shortcuts import render
import markdown2
from . import util
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from . import urls
from django.urls import reverse
from django import forms
import random
# from django.urls import redirect
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, TITLE):
    
    return render(request, "encyclopedia/showcontent.html",{
        "content": markdown2.markdown(util.get_entry(TITLE)),
        "title": TITLE
    })

# def search(request, searchkeyword):
#     stored_entries = util.list_entries()
#     ls = []
#     for entry in stored_entries:
#         if searchkeyword.lower() == entry.lower():
#             # url = urls.urlpatterns.name['index']
#             s = reverse('content', args=[searchkeyword])
            
#             return HttpResponseRedirect(s)

#             # return redirect(views.index)
            
#         else:
#             a = entry.lower()
#             z = a.find(searchkeyword)
            
#             if (z >-1):
#                 ls.append(entry)
                


def search(request):
    q = request.GET.get('q')
    
    stored_entries = util.list_entries()
    ls = []
    for entry in stored_entries:
        if q.lower() == entry.lower():
            # url = urls.urlpatterns.name['index']
            s = reverse('content', args=[q])
            
            return HttpResponseRedirect(s)

            # return redirect(views.index)
            
        else:
            a = entry.lower()
            z = a.find(q)
            
            if (z >-1):
                ls.append(entry)

 
    
    if len(ls) == 0:
        return render(request, "encyclopedia/notfound.html")
    else:
        return render(request, "encyclopedia/search.html", {
        "entries": ls
        
    })


# def s(request):
#      try:
#         q = request.GET.get('q')
#     return HttpResponseRedirect




# def viewz(request):
#     temp = util.get_entry("Git")
    
#     return render(request, "encyclopedia/temp.html", {
#         "entries": markdown2.markdown(mark_safe(temp))
#     })
    

    # mark safe ki jagha html template me use kiya hu sfe and autoescape off
    

class newcontentform(forms.Form):
    title = forms.CharField(label="Title")
    # content = forms.CharField(label="content")
    content = forms.CharField(widget=forms.Textarea, label="content")

# def addcontent(request):
#     if request.method == "POST":
#             newcontent = form.cleaned_data["content"]
#             newtitle = form.cleaned_data["title"]
#             util.save_entry(newtitle, newcontent)
#             s = reverse('content', args=[newtitle])
#             return HttpResponseRedirect(s)
#     return render(request, "encyclopedia/form.html", {
#         "form": newcontentform()
#         })


def addcontent(request):
    if request.method == "POST":
        z = request.POST
        newcontent = z["content"]
        newtitle = z["title"]
        for entry in util.list_entries():
            if entry == newtitle:
                return render(request, "encyclopedia/error.html",{
                    "content": "This content already exist",
                    "address": reverse('content', args=[newtitle]),
                    "title": newtitle
                })
        util.save_entry(newtitle, newcontent)
        s = reverse('content', args=[newtitle])
        return HttpResponseRedirect(s)
    return render(request, "encyclopedia/form.html", {
        "form": newcontentform()
        })

def rand(request):
    a = util.list_entries()
    
    z = str(random.choice(a))
    return render(request, "encyclopedia/showcontent.html",{
        "content": markdown2.markdown(util.get_entry(z)),
        "title": z
    })



def saveedit(request):
    if request.method == "POST":
        z = request.POST
        newcontent = z["content"]
        newtitle = z["title"]
        
        util.save_entry(newtitle, newcontent)
        s = reverse('content', args=[newtitle])
        return HttpResponseRedirect(s)
    



def editz(request, TITLE):
    a=util.get_entry(TITLE)
    
    return render(request, "encyclopedia/edit.html",{
        "content": util.get_entry(TITLE),
        "title": TITLE
    })

