from pyspark.sql import SparkSession

def transform_bronze_to_silver(spark):
    # TODO: Load raw JSONs from Bronze layer
    # TODO: Deduplicate records, cast data types, convert EUR amounts to DKK
    # TODO: Save to 'data/cleansed/silver_orders' as Delta/Parquet
    pass