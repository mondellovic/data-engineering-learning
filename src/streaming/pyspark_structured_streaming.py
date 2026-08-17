# Session 13 - PySpark Structured Streaming Example
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

def start_streaming_pipeline():
    spark = SparkSession.builder \
        .appName("StructuredStreamingDemo") \
        .getOrCreate()
        
    event_schema = StructType([
        StructField("event_id", StringType(), True),
        StructField("user_id", StringType(), True),
        StructField("action", StringType(), True),
        StructField("amount", DoubleType(), True),
        StructField("timestamp", TimestampType(), True)
    ])
    
    streaming_df = spark.readStream \
        .schema(event_schema) \
        .json("data/streaming_input/")
        
    aggregated_stream = streaming_df \
        .withWatermark("timestamp", "10 minutes") \
        .groupBy(
            window(col("timestamp"), "5 minutes"),
            col("action")
        ) \
        .agg({"amount": "sum", "event_id": "count"})
        
    query = aggregated_stream.writeStream \
        .format("delta") \
        .outputMode("append") \
        .option("checkpointLocation", "data/checkpoints/streaming_events") \
        .start("data/delta/streaming_events_summary")
        
    query.awaitTermination()

if __name__ == "__main__":
    pass