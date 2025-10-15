import requests
import json
import re

print('here we go!')

#
# T O K E N
# 
token = "af78906ba02b46babe0a0d80d5d5399e"

# Define the API endpoint and parameters
urlTEST = "https://api-qualif.onestock-retail.com/v3/webhooks" #old one
urlTEST = "https://c1410.api.qualif.onestock-retail.com/v3/webhooks"

urlPRO = "https://c1410.api.onestock-retail.com/v3/webhooks" 

FinalUrl = urlPRO

# Define the headers
headers = {
    'Content-Type': 'application/json'
}

# Define the data
data = {
    "site_id": "c1410",
    "token": token
}

# Make the POST request with headers and data
response = requests.get(FinalUrl, headers=headers, data=json.dumps(data))
'''
print("Request URL:", response.url)
print("Request Headers:", response.request.headers)
print("Request Body:", response.request.body)
print("Response Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Text:", response.text)
'''
# Check if the request was successful
if response.status_code == 200:
    print("Success!")
    print("Response Data:", response.json())
    respone_data = response.json()
    webhooks = respone_data.get('webhooks', [])
    counter = 0
    # Extract and print the id values
    for webhook in webhooks:
        counter = counter + 1
    
        #Check status for each one
        # Define the API endpoint and parameters

        #url = "https://c1410.api.qualif.onestock-retail.com/v3/webhooks/" + webhook['id']
        
        # FOR PROD
        url = FinalUrl + "/" + webhook['id']


        # Define the headers
        headers = {
            'Content-Type': 'application/json'
        }

        # Define the data
        data = {
            "site_id": "c1410",
            "token": token
        }
        # Make the POST request with headers and data
        response = requests.get(url, headers=headers, data=json.dumps(data))
        print(counter)

        search_value = "OneStockWebhookFunc"
        
         # Convert JSON response to string
        # response_str = json.dumps(response, indent=4)
        '''
        # Search for the text using regular expressions
        if re.search(r"OneStockWebhookFunc", response_str):
            print("Text 'OneStockWebhookFunc' found in response!")
        else:
            print("Text 'OneStockWebhookFunc' not found in response.")
        '''
        print (" - WEBHOOK ID " + webhook['id'])
        print("Response Data:", response.json())
        print( " - END WEBHOOK ID " + webhook['id'])
        print("")

else:
    print("Failed to retrieve data")
    print("Status Code:", response.status_code)
    print("Response:", response.text)

