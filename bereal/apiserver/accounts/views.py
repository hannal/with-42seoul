from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts import services
from accounts.repositories import DBRepository as Repository


__all__ = [
    'Repository',
    'signup',
]


@api_view(['POST'])
def signup(request):
    result = services.signup(request.data, Repository())
    return Response(None, status=result['code'])
