
import boto3

dynamoresource=boto3.resource('dynamodb')
table=dynamoresource.Table('switchboard')

table.put_item(Item={'switch':'cat1','status':False})
response = table.get_item(Key={'switch':'cat1'})
print (response)
