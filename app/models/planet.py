class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


planets = [
    Planet(1, "Earth", "blue planet"),
    Planet(2, "Mercury", "grey planet"),
    Planet(3, "Venus", "golden brown planet"),
    Planet(4, "Mars", "red planet"),
    Planet(5, "Jupiter", "yellow, brown, red planet"),
    Planet(6, "Saturn", "yellow, brown, grey planet"),
    Planet(7, "Uranus", "cyan planet"),
    Planet(8, "Neptune", "blue"),
]


"""
Possible questions:
1. Should ID be out of generated or it coming as a argument
- if out, in this case I'll use a random number
2. Does the planets has an additional atributes like a moons or any other parametrs?
- if so, we should include it in our planet list. If not for now, we can add later


to check:
http://127.0.0.1:5000/planets/
output:
[{"description":"blue planet","id":1,"name":"Earth"},
{"description":"grey planet","id":2,"name":"Mercury"},
{"description":"golden brown planet","id":3,"name":"Venus"},
{"description":"red planet","id":4,"name":"Mars"},
{"description":"yellow, brown, red planet","id":5,"name":"Jupiter"},
{"description":"yellow, brown, grey planet","id":6,"name":"Saturn"},
{"description":"cyan planet","id":7,"name":"Uranus"},
{"description":"blue","id":8,"name":"Neptune"}]
"""
