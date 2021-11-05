from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView, ListView

from blog.models import Post
from properties.models import CardsFeatures, CardsProgramUnits, CardDoxHome, CardEliteHome, SubCategory, \
    DetailSubCategory, Category


def home(request):
    posts = Post.objects.all()
    cards_dox = CardDoxHome.objects.all()
    cards_elite = CardEliteHome.objects.all()
    return render(request, 'home/index.html', {
        'posts': posts,
        'cards_dox': cards_dox,
        'cards_elite': cards_elite,
    })


def nav(request, slug):
    if slug in ['dox-solutions', 'doxerp', 'doxbook', 'doxcustomize']:
        sub_category = SubCategory.objects.all()[:3]
    else:
        sub_category = SubCategory.objects.all()[3:]
    details = DetailSubCategory.objects.filter(category__slug=slug)
    cards_features = CardsFeatures.objects.filter(category__slug=slug)
    cards_units = CardsProgramUnits.objects.filter(category__slug=slug)
    return render(request, 'details/category-page-dox.html',
        {
            'sub_category': sub_category,
            'details': details,
            'cards_features': cards_features,
            'cards_units': cards_units,
        })

