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
