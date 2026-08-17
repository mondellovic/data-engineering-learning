import json, requests, os

def run_metadata_ingestion(config_path="src/orchestration/metadata/control_table.json"):
    with open(config_path) as f:
        sources = json.load(f)
    
    for source in sources:
        response = requests.get(source["endpoint"])
        os.makedirs(f"data/{source['target_path']}", exist_ok=True)
        with open(f"data/{source['target_path']}data.json", "w") as f_out:
            json.dump(response.json(), f_out)
        print(f"Ingested {source['source_name']}")

if __name__ == "__main__":
    run_metadata_ingestion()