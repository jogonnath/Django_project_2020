from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from listings.model_choices import state_choices,bedroom_choices,price_choices
# pages app views
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    latest = Listing.objects.order_by('-list_date')[:3]


    context = {
        'latest': latest,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request,'pages/index.html', context)

def about(request):
    team = Realtor.objects.order_by('-contact_date')[:3]
    seller_of_month = Realtor.objects.filter(is_mvp = True).first()

    context = {
        'team': team,
        'seller_of_month': seller_of_month
    }

    return render(request, 'pages/about.html', context)

def featured(request):

    featured_list = Listing.objects.filter(is_published=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(featured_list, 3)

    try:
        featured_list = paginator.page(page)

    except PageNotAnInteger:
        # fall back to first page
        featured_list = paginator.page(1)
    except EmptyPage:
        # fall back to last page
        featured_list = paginator.page(paginator.num_pages)
    context = {
        'featured_list': featured_list
    }
    return render(request, 'pages/featured.html', context)
