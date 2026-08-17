# Azure Data Engineering Mastery Journey

Dette repository indeholder min læringsrejse, kodeeksempler, Infrastructure as Code (IaC) og praktiske øvelser i overgangen fra klassisk ETL (SQL/SSIS) til en moderne cloud-baseret **Data Platform Architecture** på Azure & Databricks.

## Fokusområder
- **Storage & Ingestion:** Azure Data Lake Storage Gen2, Azure Data Factory (Metadata-driven).
- **Compute & Processing:** Apache Spark, PySpark, Databricks, Delta Lake.
- **Architecture Patterns:** Lakehouse, Medallion Architecture (Bronze/Silver/Gold), Data Vault 2.0, Star Schema.
- **Transformation & Quality:** dbt (data build tool), Great Expectations, Data Contracts.
- **DevOps & IaC:** Azure Bicep, GitHub Actions CI/CD.

azure-data-engineering-learning/
├── .github/
│   └── workflows/
│       └── python-tests.yml                  # GitHub Actions CI pipeline
├── docs/
│   ├── LEARNING_JOURNAL.md                  # Din løbende logbog for alle 15 sessions
│   └── architecture-diagrams/               # Til arkitektur- og flowdiagrammer
├── infrastructure/
│   └── bicep/
│       ├── main.bicep                       # IaC: ADLS Gen2, Key Vault, ADF
│       └── parameters.json                  # Bicep deployment parametre
├── src/
│   ├── adf/
│   │   ├── pipelines/
│   │   │   └── pipeline_metadata_ingestion.json # Dynamic metadata-driven ingestion
│   │   └── linkedServices/
│   ├── databricks/
│   │   ├── bronze/
│   │   │   └── ingest_raw_data.py           # Raw -> Bronze Delta with metadata
│   │   ├── silver/
│   │   │   └── transform_cleansed_data.py   # Bronze -> Silver (Deduplication & Delta MERGE)
│   │   └── gold/
│   │       └── aggregate_business_marts.py  # Silver -> Gold (Star Schema / Aggregations)
│   ├── dbt_project/
│   │   ├── models/
│   │   │   ├── staging/
│   │   │   │   └── stg_orders.sql           # dbt Staging transformationer
│   │   │   ├── intermediate/
│   │   │   ├── marts/
│   │   │   │   └── fct_orders.sql           # dbt Fact table model
│   │   │   └── schema.yml                   # dbt tests & dokumentation
│   │   ├── dbt_project.yml                  # dbt projektkonfiguration
│   │   └── profiles.yml                     # Local DuckDB profile for dbt
│   └── streaming/
│       └── pyspark_structured_streaming.py  # Real-time event streaming pipeline
├── tests/
│   ├── unit/
│   │   └── test_pyspark_transformations.py  # PyTest til PySpark unit testing
│   └── integration/
├── .gitignore
├── README.md                                # Projektoversigt & session-status
└── requirements.txt                         # Dependencies (pyspark, delta-spark, dbt, pytest)

## Oversigt over Sessions
| Session | Emne | Status | Kode / Noter |
|---|---|---|---|
| **01** | Cloud Storage & IaC (Bicep) | ⏳ Planlagt | [Note](docs/session-notes/session-01.md) \| [Code](infrastructure/bicep/) |
| **02** | Azure Data Factory Orchestration | ⏳ Planlagt | [Note](docs/session-notes/session-02.md) \| [Code](src/adf/) |
| **03** | Metadata-Driven Ingestion | ⏳ Planlagt | [Note](docs/session-notes/session-03.md) \| [Code](src/adf/) |
| **04** | Databricks & Delta Lake Core | ⏳ Planlagt | [Note](docs/session-notes/session-04.md) \| [Code](src/databricks/) |
| **05** | PySpark Architecture & Tuning | ⏳ Planlagt | [Note](docs/session-notes/session-05.md) \| [Code](src/databricks/) |
| **06** | Advanced PySpark & Window Funcs | ⏳ Planlagt | [Note](docs/session-notes/session-06.md) \| [Code](src/databricks/) |
| **07** | Medallion Architecture | ⏳ Planlagt | [Note](docs/session-notes/session-07.md) \| [Code](src/databricks/) |
| **08** | Dimensional Modeling & SCD2 | ⏳ Planlagt | [Note](docs/session-notes/session-08.md) \| [Code](src/databricks/) |
| **09** | Data Vault 2.0 vs. Star Schema | ⏳ Planlagt | [Note](docs/session-notes/session-09.md) |
| **10** | Transformation with dbt | ⏳ Planlagt | [Note](docs/session-notes/session-10.md) \| [Code](src/dbt_project/) |
| **11** | Data Quality & Data Contracts | ⏳ Planlagt | [Note](docs/session-notes/session-11.md) \| [Code](tests/) |
| **12** | CI/CD Pipelines (GitHub Actions) | ⏳ Planlagt | [Note](docs/session-notes/session-12.md) \| [Code](.github/workflows/) |
| **13** | PySpark Structured Streaming | ⏳ Planlagt | [Note](docs/session-notes/session-13.md) \| [Code](src/streaming/) |
| **14** | Governance & Unity Catalog | ⏳ Planlagt | [Note](docs/session-notes/session-14.md) |
| **15** | Production Operations | ⏳ Planlagt | [Note](docs/session-notes/session-15.md) |

---
*Opdateret løbende under læringsforløbet.*