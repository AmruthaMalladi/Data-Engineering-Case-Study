class ConfigLoader:
    def __init__(self, path):
        self.path = path
    
    def load_config(self):
        # Assuming JSON config for simplicity, stored in S3
        config_df = spark.read.json(self.path)
        return config_df.collect()[0].asDict(recursive=True)
