from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view()
def product_list(request):
    """ Returning list of product """
    return Response('OK')


@api_view()
def product_detail(request, id):
    """ show the detail of product """
    return Response(f'OK {id}')
