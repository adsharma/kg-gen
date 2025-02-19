from relik import Relik
from kg_gen.models import Graph
import os
import json


relik = Relik.from_pretrained("relik-ie/relik-cie-small", device="cuda")

os.makedirs("KGs", exist_ok=True)

with open("essays.json", "r") as f:
    data = json.load(f)
    counter = 1
    for essay in data:
        print(f"{counter}: {essay['topic']}")
        try:
            out = relik(essay["content"])
            entities = [s.label for s in out.spans]
            triplets = [
                [t.subject.label, t.label, t.object.label] for t in out.triplets
            ]
            edges = {p for (_, p, _) in triplets}
            graph = Graph(entities=entities, edges=edges, relations=triplets)
            json_out = graph.model_dump_json()
        except Exception as e:
            print(e)
            json_out = '{"error": "true"}'
        with open(f"KGs/{counter}.json", "w") as fw:
            fw.write(json_out)
        counter += 1
