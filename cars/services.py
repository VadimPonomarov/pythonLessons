from django.db.models import QuerySet
from rest_framework.request import Request

car_filters = {
    'year': 'year',
    'year_gt': 'year__gt',
    'year_lt': 'year__lt',
    'year_gte': 'year__gte',
    'year_lte': 'year__lte',
    'year_exact': 'year__exact',

    'price': 'price',
    'price_gt': 'price__gt',
    'price_lt': 'price__lt',
    'price_gte': 'price__gte',
    'price_lte': 'price__lte',
    'price_exact': 'price__exact',

    'brand': 'brand__icontains'
}


def set_filter(qs: QuerySet, request: Request):
    params = request.query_params
    print(params)
    for key, val in params.items():
        if key in car_filters:
            qs = qs.filter(**{car_filters.get(key): val})
    return qs
