from properties.models import Category


def category(request):
    categories_base = Category.objects.all()
    return {'categories_base': categories_base}
