#!/usr/bin/env python3
import requests

# Keycloak configuration
KEYCLOAK_URL = "https://iam.nexiona.io/realms/learning-nestor/protocol/openid-connect/token"
CLIENT_ID = "next-keycloak"
CLIENT_SECRET = "xY4ZFLW4JWrzslFpJq1TVR2YK1tosDZq"

# NGINX protected resource
API_URL = "http://mimir.learn.keycloak.nexiona.io/prometheus/api/v1/label/__name__/values"
#API_URL = "http://mimir.learn.keycloak.nexiona.io/services"

def get_access_token():
    """ Obtain the access token from Keycloak using client credentials. """
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials',
        'scope': 'openid profile email'
    }
    response = requests.post(KEYCLOAK_URL, data=payload)
    response_data = response.json()
    return response_data['access_token']

def access_protected_resource(access_token):
    """ Access the protected API with the obtained access token. """
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(API_URL, headers=headers)
    return response.status_code, response.text

def main():
    try:
        # Get access token from Keycloak
        access_token = get_access_token()
        print(f"Access Token: {access_token}\n")

        # Access protected resource
        status_code, content = access_protected_resource(access_token)
        print(f"Response Status Code: {status_code}")
        print(f"Response Content: {content}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
