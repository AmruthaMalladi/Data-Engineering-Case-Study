from ingestion.configLoader import ConfigLoader

def create_kafka_source(config):
    return spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", config["kafka_servers"]) \
        .option("subscribe", config["topic"]) \
        .option("startingOffsets", "earliest") \
        .load()

def apply_schema_and_transformations(df, schema_config, transformations):
    # Apply schema
    schema = StructType.fromJson(schema_config)
    df = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("data")).select("data.*")

    # Apply transformations based on configuration
    for transformation in transformations:
        if transformation["type"] == "rename":
            df = df.withColumnRenamed(transformation["old_name"], transformation["new_name"])
    
    return df



if __name__ == "__main__":
    config_path = "path/to/config.json"
    config_loader = ConfigLoader(config_path)
    config = config_loader.load_config()

    # Kafka source
    kafka_df = create_kafka_source(config)

    # Apply schema and transformations
    processed_df = apply_schema_and_transformations(kafka_df, config["schema"], config["transformations"])

    # Define the query and output mode
    query = processed_df \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()
