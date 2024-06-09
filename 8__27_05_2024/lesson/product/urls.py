from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('store/<int:store_id>', store, name='store'),
    path('add', add_categ, name='add'),
    path('change_categ/<int:categ_id>', change_categ, name='change_categ'),
    path('change_categ_confirm', change_categ_confirm, name='change_categ_confirm'),
    path('delete_categ/<int:categ_id>', delete_categ, name='delete_categ'),
    path('view_posts_categ/<int:categ_id>', view_posts_categ, name='view_posts_categ'),
    path('add_product', add_product, name='add_product'),
    path('update_product/<int:id>', update_product, name='update_product'),
    path('update_product_confirm', update_product_confirm, name='update_product_confirm'),
    path('delete_product/<int:id>', delete_product, name='delete_product'),
]
