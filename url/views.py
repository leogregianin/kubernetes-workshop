import hashlib

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import URL
from .serializers import URLSerializer
from .utils import valid_url


def redirect_original_url(request, hash):
    try:
        url = URL.objects.get(hash=hash)
        url.visits += 1
        url.save()
        return redirect(valid_url(url=url.url))
    except URL.DoesNotExist:
        return HttpResponseNotFound("Short URL not found")

@csrf_exempt
@api_view(['POST'])
def create_short_url(request):
    if 'url' in request.data:
        original_url = valid_url(url=request.data['url'])

        # Generate a unique hash for the URL
        hash_value = hashlib.md5(original_url.encode()).hexdigest()[:10]

        # Create a new URL object in the database
        url = URL.objects.create(hash=hash_value, url=original_url)

        # Return the shortened URL in the response
        return JsonResponse(
            {'short_url': f'/url/{hash_value}/'},
            status=status.HTTP_201_CREATED
        )

    return JsonResponse(
        {'error': 'Invalid request data'},
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['GET'])
def get_url_stats(request, hash):
    try:
        url = URL.objects.get(hash=hash)
        serializer = URLSerializer(url)
        return Response(serializer.data)
    except URL.DoesNotExist:
        return Response(
            {'error': 'Short URL not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
def simple_ui(request):
    urls = URL.objects.all()
    return render(request, "index.html", {"urls": urls})