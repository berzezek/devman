import json

from django.shortcuts import get_object_or_404, render

from places.models import Place
from places.utils import set_features


def index(request):
    """
    Renders the index page with a GeoJSON representation of all places.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered index page.
    """
    places = Place.objects.all()

    features = set_features(places, request)

    geojson = json.dumps({"type": "FeatureCollection", "features": features})

    return render(request, "places/index.html", {"geojson": geojson})


def place_detail(request, place_id):
    """
    Renders the place detail page.

    Args:
        request (HttpRequest): The HTTP request object.
        place_id (int): The id of the place.

    Returns:
        HttpResponse: The HTTP response object containing the rendered place detail page.
    """
    place = get_object_or_404(Place, pk=place_id)

    return render(request, "places/detail.html", {"place": place})


def place_detail_serializer(request, place_id):
    """
    Serializes the details of a place.

    Args:
        request (HttpRequest): The HTTP request object.
        place_id (int): The ID of the place.

    Returns:
        HttpResponse: The rendered response containing the serialized place data.
    """
    place = Place.objects.get(pk=place_id)

    images = [
        request.build_absolute_uri(image.image.url) for image in place.images.all()
    ]

    place_data = {
        "title": place.title,
        "imgs": images,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.longitude, "lat": place.latitude},
    }

    return render(request, "places/serialize_detail.html", {"place_data": place_data})
