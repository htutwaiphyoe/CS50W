actors = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Luna", "house": "RavenClaw"},
    {"name": "Draco", "house": "Slytherine"},
]

actors.sort(key = lambda actor: actor["name"])

print(actors)