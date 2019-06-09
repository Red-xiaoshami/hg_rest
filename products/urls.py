from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^products/$',
        views.ProductList.as_view(),
        name="product_list"),

    url(r'^products/(?P<pk>\d+)/$',
        views.ProductDetail.as_view(),
        name="product_detail"),

    url(r'^category/$',
        views.CategoryViewSet.as_view(),
        name="category_list"),
]


# urlpatterns = format_suffix_patterns(urlpatterns)