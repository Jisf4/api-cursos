import boto3

def lambda_handler(event, context):
    # Entrada (json)
    curso = event['body']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Cursos')
    response = table.put_item(Item=curso)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
