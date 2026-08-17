# Databricks Notebook: Bronze Layer Ingestion
# Session 04 / Session 07 - Raw Data Ingestion to Delta Lake

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, input_file_name

def ingest_raw_to_bronze(spark: SparkSession, source_path: str, target_delta_path: str):
    """
    Reads raw JSON files from ADLS Gen2 'raw' container and appends them
    to Bronze Delta table with metadata fields (ingestion timestamp & source filename).
    """
    print(f"Reading raw data from: {source_path}")
    
    # Read raw JSON files
    raw_df = spark.read.format("json").load(source_path)
    
    # Add metadata columns (Auditability pattern)
    bronze_df = raw_df \
        .withColumn("_ingested_at", current_timestamp()) \
        .withColumn("_source_file", input_file_name())
    
    # Append to Delta Lake Bronze table
    print(f"Writing to Bronze Delta table at: {target_delta_path}")
    bronze_df.write \
        .format("delta") \
        .mode("append") \
        .option("mergeSchema", "true") \
        .save(target_delta_path)
        
    print("Bronze ingestion completed successfully.")

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("BronzeIngestion") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .getOrCreate()