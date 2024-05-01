import pymysql
import boto3
from smb.SMBConnection import SMBConnection

class DataConnector:
    def __init__(self, config):
        self.config = config

    def connect(self):
        source_type = self.config['type']
        if source_type == 'sql':
            return self.connect_to_sql()
        elif source_type in ['s3', 'gcs', 'azure']:
            return self.connect_to_cloud_storage()
        elif source_type == 'file_server':
            return self.connect_to_file_server()
        else:
            raise ValueError("Unsupported source type")

    def connect_to_sql(self):
        return pymysql.connect(
            host=self.config['host'],
            user=self.config['user'],
            password=self.config['password'],
            db=self.config['db']
        )

    def connect_to_cloud_storage(self):
      try:
        if self.config['type'] == 's3':
            return boto3.resource('s3')
        else if self.config['type'] == 'gcs':
            return boto3.resource('gcs')
        else self.config['type'] == 'azure':
            return boto3.resource('azure')
      except ConnectionError as CX:
        raise CX

    def connect_to_file_server(self):
        return SMBConnection(
            self.config['user'], 
            self.config['password'], 
            self.config['client_machine_name'], 
            self.config['server_name'], 
            use_ntlm_v2=True
        )
