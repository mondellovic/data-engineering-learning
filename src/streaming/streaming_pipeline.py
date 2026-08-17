from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, expr

spark = SparkSession.builder.appName("Session13-Streaming").getOrCreate()

# Read stream from raw clickstream folder
df_stream = spark.readStream.schema("timestamp STRING, user_id INT, event_type STRING, product_id INT").json("data/raw/clickstream/")

# TODO: Apply 10-minute watermark and tumbling 5-minute window aggregations