
import boto3

dynamoresource=boto3.resource('dynamodb')
table=dynamoresource.Table('Monsters')

print(table.get_item(Key={'Name':'BoYo'}))
table.put_item(Item={'Name':'BoYo','Age':'Baby'})


