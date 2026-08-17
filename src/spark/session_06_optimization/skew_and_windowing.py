from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast, window, col, row_number
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("Session06-Optimization").getOrCreate()

# TODO: Generate skewed order data for B2B customer (ID: 9999)
# TODO: Compare standard join vs broadcast join: df_orders.join(broadcast(df_products), "product_id")
# TODO: Implement window functions for cumulative customer spending