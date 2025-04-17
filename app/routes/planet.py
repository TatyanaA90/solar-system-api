from flask import Blueprint
from app.models.planet import planets
from app.routes.helpers import validate_planet

planets_bp = Blueprint("planents_bp", __name__, url_prefix="/planets")

# wave_1
@planets_bp.get("/")
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
                {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description
                }
        )
    return planets_response

# wave_2
@planets_bp.get("/<id>")
def get_one_planet(id):
    planet = validate_planet(id)
    return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description   
            } # , 201  --> if we add code status here we can change the output from default 200 to what we need


# http://127.0.0.1:5000/planets/2
# {"description":"grey planet","id":2,"name":"Mercury"}

