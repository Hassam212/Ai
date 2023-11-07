from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ItemForm
from .models import Item


# Create your views here.

def index(request):
    all_items = Item.objects.all()

    unique_items = set()

    item_list = []
    for item in all_items:
        if item.item_head not in unique_items:
            unique_items.add(item.item_head)
            item_list.append(item)
    ######################

    template = loader.get_template('blog/index.html')
    context = {
        'item_list': item_list,

    }

    return HttpResponse(template.render(context, request))


def card(request):
    item_list = Item.objects.all()
    template = loader.get_template('blog/card.html')
    context = {
        'item_list': item_list,

    }
    return HttpResponse(template.render(context, request))


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('blog:index')

    return render(request, 'blog/item-form.html', {'form': form})


def detail(request, item_id):
    sections = Item.objects.get(pk=item_id)
    item_list = Item.objects.filter(item_head=sections)

    context = {
        'item_list': item_list,
    }

    return render(request, 'blog/detail.html', context)


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Item.objects.filter(item_head=searched)
        context = {
            'searched': searched,
            'venues': venues,
        }
        return render(request, 'blog/search.html', context)
    else:
        context = {

        }
        return render(request, 'blog/search.html', context)
