from django.shortcuts import render
import json
from .models import Place
from places.utils import create_features


def index(request):
    """
    Renders the index page with a GeoJSON representation of all places.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered index page.
    """
    places = Place.objects.all()

    features = create_features(places, request)

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
    place = Place.objects.get(pk=place_id)

    return render(request, "places/detail.html", {"place": place})


def place_detail_serializer(request, place_id):

    place = Place.objects.get(pk=place_id)
    place_images = place.placeimage_set.all()
    images = [request.build_absolute_uri(image.image.url) for image in place_images]

    # serialize the place
    place_data = {
        "title": place.title,
        "imgs": images,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.longitude, "lat": place.latitude},
    }

    return render(request, "places/serialize_detail.html", {"place_data": place_data})
