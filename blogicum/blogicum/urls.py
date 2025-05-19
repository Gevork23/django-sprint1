from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render


def custom_page_not_found_view(request, exception):
    return render(request, "blog/404.html", status=404)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("pages/", include("pages.urls")),
]

handler404 = 'blogicum.urls.custom_page_not_found_view'
