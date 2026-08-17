import logging, json
from datetime import datetime

class JsonLogger:
    @staticmethod
    def log_info(pipeline_name, processed_rows, status="SUCCESS"):
        log_payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "pipeline": pipeline_name,
            "processed_rows": processed_rows,
            "status": status
        }
        print(json.dumps(log_payload))

if __name__ == "__main__":
    JsonLogger.log_info("silver_orders_ingestion", 1500)