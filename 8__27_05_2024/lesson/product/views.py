from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.text import slugify

from .models import Store, Category, Product


# Create your views here.

def index(request):
    search = request.GET.get('search') or ''
    shops = Store.objects.filter(name__icontains=search)

    return render(request, 'product/index.html', context={'shops': shops})


def store(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    category = Category.objects.all()
    # print(category)

    cntx = {
        'category': category,
        'store': store
    }

    return render(request, 'product/store.html', context=cntx)


def add_categ(request):
    categ_name = request.POST.get('store_name')
    # print(categ_name)

    category = Category()
    category.name = categ_name
    category.slug = slugify(category.name)
    category.save()
    # return redirect('store', store_id=1)

    return redirect(request.META.get('HTTP_REFERER'))


def change_categ(request, categ_id):
    category = get_object_or_404(Category, pk=categ_id)
    category_id = categ_id

    cntx = {
        'category': category,
        'id': category_id
    }

    return render(request, 'product/change_categ.html', context=cntx)


def change_categ_confirm(request):
    category_id = request.POST.get('category_id')
    new_category_name = request.POST.get('category_name')

    print('aasdasds' + category_id)

    category = get_object_or_404(Category, pk=category_id)
    category.name = new_category_name
    category.save()

    return redirect('index')


def delete_categ(request, categ_id):
    category = get_object_or_404(Category, pk=categ_id)
    category.delete()
    return redirect('index')


def view_posts_categ(request, categ_id):
    categ = Category.objects.all()
    category = get_object_or_404(Category, pk=categ_id)
    products = Product.objects.filter(category=category)
    return render(request, 'product/view_post_categ.html', context={'products': products, "categ":categ})




def add_product(request):
    categ_id = request.POST.get('categ_id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    slug = request.POST.get('slug')

    category = Category.objects.get(pk=categ_id)

    product = Product(name=name, price=price, category=category, slug=slug)
    product.save()

    return redirect('index')



def update_product(request, id):

    product = get_object_or_404(Product, pk=id)
    category = Category.objects.all()

    return render(request, 'product/update_product.html', context={'product': product, "category":category})


def update_product_confirm(request):
    product_id = request.POST.get('product_id')
    categ_id = request.POST.get('categ_id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    slug = request.POST.get('slug')
    category = Category.objects.get(pk=categ_id)

    product = Product.objects.get(pk=product_id)
    product.name = name
    product.price = price
    product.category = category
    product.slug = product.slug
    product.save()

    return redirect('index')


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('index')