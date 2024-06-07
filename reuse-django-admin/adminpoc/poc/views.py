from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


@staff_member_required
def index(request):
    vars = dict(has_permission = True, site_url = "/")
    return render(request, "poc/index.html", vars)
