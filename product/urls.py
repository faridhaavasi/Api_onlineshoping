from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('category_list', views.CategoryListView.as_view(), name='category_list'),
]

