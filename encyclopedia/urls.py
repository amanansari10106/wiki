from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("a/", views.viewz, name="viewz")
    path("wiki/<str:TITLE>", views.content, name="content"),
    path("wiki/new/add/", views.addcontent, name="add"),
    path("wiki/new/rand/", views.rand, name="rand"),
    path("wiki/new/edit/<str:TITLE>", views.editz, name="edit"),
    path("wiki/new/saveedit", views.saveedit, name="saveedit"),
    # path("wiki/search/<str:searchkeyword>", views.search, name="searchkeyword"),
    # path("wiki/search/<str:q>", views.search, name="s")
    url(r'^wiki/search/$', views.search, name="s")


    

]
