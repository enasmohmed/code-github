from properties.models import Category, SubCategory


def category(request):
    categories_base = Category.objects.all()
    sub_category_base = SubCategory.objects.all()
    return {'categories_base': categories_base, 'sub_category_base': sub_category_base}
