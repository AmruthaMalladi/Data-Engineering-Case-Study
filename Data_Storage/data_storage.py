from pyspark.sql import SparkSession

def data_storage():
    spark = SparkSession.builder.appName("AdStorage").getOrCreate()
    # Processed dataframes
    processed_data = ...
    # Write to storage
    processed_data.write.mode('overwrite').parquet("hdfs://path/to/processed_data.parquet")

if __name__ == "__main__":
    data_storage()
