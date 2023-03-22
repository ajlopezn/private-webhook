import functions_framework

@functions_framework.http
def hello_http(request):
    """
    HTTP Cloud Function that makes another HTTP request.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    
    pubsub_message = request.get_json()
    print('received request')
    print(pubsub_message)
   
    import requests
    
    # internal webhook endpoint. May be placed in your VPC or OnPrem. Serverless Connector and Routes / Firewall Rules are required. 
    url = 'http://10.128.0.4'

    # Process the request
    # response = requests.get(url)
    response = requests.post(url, json = pubsub_message)
    print(response.raise_for_status)
    print(response.content)

    return 'Success!'
# [END functions_concepts_requests]
