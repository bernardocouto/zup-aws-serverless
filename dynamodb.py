import boto3


class DynamoDB():

    def __init__(self):
        self.resource = boto3.resource('dynamodb')
        self.table_name = 'zup-aws-serverless'

    def get_item(self, partition_key: dict):
        table = self.resource.Table(self.table_name)
        return table.get_item(Key=partition_key)

    def put_item(self, item: dict):
        table = self.resource.Table(self.table_name)
        table.put_item(Item=item)
