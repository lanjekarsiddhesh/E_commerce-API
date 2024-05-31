from django_filters.rest_framework import FilterSet
from productApp.models import *


class productFilters(FilterSet):
    class Meta:
        model = Product
        fields = {
            'Category': ['exact'],
            'subCategory': ['exact'],
            'company_id': ['exact'],
            'price': ['lte', 'gte'],

        }




            
