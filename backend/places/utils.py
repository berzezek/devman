from places.models import PlaceImage
import json


def create_features(places: list, request) -> list:
    """
    Create a list of features for each place.

    Args:
        places (list): A list of places.
        request: The request object.

    Returns:
        list: A list of features, each representing a place.
    """
    features = []

    for place in places:
        
        # get all images for the place
        images = PlaceImage.objects.filter(place=place)
        
        # sort images by image_number
        images = sorted(images, key=lambda image: image.image_number)
        
        # get absolute urls for images and create a list of them
        imgs = [request.build_absolute_uri(image.image.url) for image in images]

        # create a dictionary with details for the place
        details_url = {
            "title": place.title,
            "imgs": imgs,
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {"lng": place.longitude, "lat": place.latitude},
        }
        
        
        # write the details to a json file
        with open(f"static/assets/places/{place.pk}.json", "w") as file:
            file.write(json.dumps(details_url))

            features.append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            place.latitude,
                            place.longitude,
                        ],
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.pk,
                        "detailsUrl": f"./{file.name}",
                    },
                }
            )
    return features