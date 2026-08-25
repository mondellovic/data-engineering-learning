# Nordic Retail Group — Data Engineering Learning Path

Hands-on repository containing practical implementation tasks, data pipelines, infrastructure scripts, and transformations across all course sessions.

---

## Project Structure

```text
.
├── .github/workflows/      # Session 12: CI/CD GitHub Actions
├── data/raw/               # Raw ingested sources (products, customers, orders, clickstream)
├── infrastructure/bicep/   # Session 1: Azure Bicep IaC provisioning
├── src/
│   ├── governance/         # Session 14: Access control & governance policies
│   ├── models/
│   │   ├── datavault/      # Session 9: Data Vault 2.0 implementation
│   │   ├── dimensional/    # Session 8: SCD Type 2 Customer dimension
│   │   └── medallion/      # Session 7: Bronze, Silver, & Gold Delta pipelines
│   ├── operations/         # Session 15: Structured logging & error alerting
│   ├── orchestration/      # Session 2 & 3: ADF configs & metadata-driven ingestion
│   ├── quality/            # Session 11: Data contracts & quarantine logic
│   ├── spark/              # Sessions 4, 5, 6: Delta operations & execution tuning
│   ├── streaming/          # Session 13: Real-time event generation & streaming
│   ├── transformations/    # Session 10: dbt models (staging & marts)
│   └── utils/              # Data generation helper scripts
├── tests/                  # Session 12: Unit tests for data pipelines
└── requirements.txt        # Python dependency manifest

```

# QUICKSTART
## Create virtual environment
python -m venv .venv

## Activate environment (Linux/macOS)
source .venv/bin/activate
## On Windows use: .venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

# GENERATE SAMPLE DATA
## Generate initial orders data
python src/utils/generate_orders.py

## Run streaming event generator (for Session 13)
python src/streaming/event_generator.py

# RUNNING DATA QUALITY TESTS
pytest tests/

##test