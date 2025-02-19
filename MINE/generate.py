from kg_gen import KGGen
import json

# Initialize KGGen with optional configuration
kg = KGGen(
    model="your-model",
    temperature=0.0,  # Default temperature
)

with open("essays.json", "r") as f:
    data = json.load(f)
    counter = 1
    for essay in data:
        print(f"{counter}: {essay['topic']}")
        try:
            graph = kg.generate(
                input_data=essay["content"],
                context=essay["topic"],
            )
            json_out = graph.model_dump_json()
        except Exception as e:
            json_out = '{"error": "true"}'
        with open(f"KGs/{counter}.json", "w") as fw:
            fw.write(json_out)
        counter += 1
