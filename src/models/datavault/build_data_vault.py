from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, concat_ws, col

# TODO: Load Customer sources from Danish and Swedish feeds
# TODO: Compute Hub Hash Keys: sha2(col("email"), 256)
# TODO: Populate Hub_Customer, Link_Order, and Satellite_Customer_Details tables