from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from items.models import item

@login_required
def index(request):
    items = item.objects.filter(created_by = request.user)

    return render(request, "Dashboard/index.html", {
        'items':items
    })



