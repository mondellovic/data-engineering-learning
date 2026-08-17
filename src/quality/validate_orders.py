import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Session11-Quality").getOrCreate()

def validate_orders(input_path):
    df = spark.read.json(input_path)
    
    # Quarantine rows violating Data Contract
    valid_df = df.filter(col("order_id").isNotNull() & (col("total_amount") > 0))
    quarantine_df = df.filter(col("order_id").isNull() | (col("total_amount") <= 0))
    
    # TODO: Write valid_df to Silver and quarantine_df to Quarantine directory