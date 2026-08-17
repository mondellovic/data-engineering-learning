# Unit Tests for PySpark Transformations
# Session 11 / Session 12 - Testing Pipelines with PyTest

import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .master("local[1]") \
        .appName("UnitTestSession") \
        .getOrCreate()

def test_pyspark_data_cleansing(spark):
    schema = StructType([
        StructField("id", StringType(), True),
        StructField("amount", DoubleType(), True)
    ])
    
    data = [("1", 100.0), ("2", None), ("3", 300.0)]
    df = spark.createDataFrame(data, schema)
    
    # Filter out nulls
    cleaned_df = df.filter(df.amount.isNotNull())
    
    assert cleaned_df.count() == 2
    assert "amount" in cleaned_df.columns