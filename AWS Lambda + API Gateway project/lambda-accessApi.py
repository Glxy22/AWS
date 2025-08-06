import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    try:
        print("Event received:", json.dumps(event))
        
        # Extract HTTP method from HTTP API event format v2.0
        http_method = event.get('requestContext', {}).get('http', {}).get('method')
        
        if not http_method:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing HTTP method in event'})
            }

        if http_method == 'POST':
            if 'body' not in event or not event['body']:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Missing request body'})
                }

            body = json.loads(event['body'])
            name = body.get('name')
            email = body.get('email')
            user_class = body.get('class', '5th')

            if not name or not email:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Missing name or email'})
                }

            table.put_item(
                Item={
                    'email': email,
                    'name': name,
                    'class': user_class
                }
            )

            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'User added successfully'})
            }

        elif http_method == 'GET':
            response = table.scan()
            users = response.get('Items', [])

            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps(users)
            }

        else:
            return {
                'statusCode': 405,
                'body': json.dumps({'error': f'Method {http_method} not allowed'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
