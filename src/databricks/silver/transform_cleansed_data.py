# Databricks Notebook: Silver Layer Transformation
# Session 07 / Session 08 - Cleansing, Deduplication and Delta MERGE

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window
from delta.tables import DeltaTable

def transform_bronze_to_silver(spark: SparkSession, bronze_path: str, silver_path: str, key_col: str):
    """
    Reads Bronze Delta table, performs deduplication & data type conversions,
    and upserts into Silver Delta table using Delta MERGE.
    """
    print(f"Reading Bronze data from: {bronze_path}")
    bronze_df = spark.read.format("delta").load(bronze_path)
    
    # Deduplication using Window functions
    window_spec = Window.partitionBy(key_col).orderBy(col("_ingested_at").desc())
    dedup_df = bronze_df \
        .withColumn("row_num", row_number().over(window_spec)) \
        .filter(col("row_num") == 1) \
        .drop("row_num")
    
    # Perform Delta MERGE (Upsert)
    if DeltaTable.isDeltaTable(spark, silver_path):
        silver_table = DeltaTable.forPath(spark, silver_path)
        
        silver_table.alias("target") \
            .merge(
                dedup_df.alias("source"),
                f"target.{key_col} = source.{key_col}"
            ) \
            .whenMatchedUpdateAll() \
            .whenNotMatchedInsertAll() \
            .execute()
        print("Silver table updated via Delta MERGE.")
    else:
        print("Silver table does not exist. Creating initial Silver Delta table...")
        dedup_df.write.format("delta").mode("overwrite").save(silver_path)

if __name__ == "__main__":
    spark = SparkSession.builder.appName("SilverTransformation").getOrCreate()