from blog.models import Category


def category_list(request):
    """ Function to display category names in navbar site wise """
    categories = Category.objects.all()
    return {'categories': categories}
