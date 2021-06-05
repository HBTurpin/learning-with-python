import requests

#https://humblebundlenotifications.azurewebsites.net/api/RegisterWebhook
#https://humblebundlenotifications.azurewebsites.net/api/TestWebhook
url = 'https://humblebundlenotifications.azurewebsites.net/api/TestWebhook'
header = {"Content-Type": "application/json"}
json = {
    "type": 0,
    "webhook": "https://discord.com/api/webhooks/844251693742424106/EUHZxYc_7_sdcUbRz6ASR0ZhWS7qGjYx-x0F4IBsb0RJtTFqrZmPqNJKNR8w5-NQf8RO",
    "sendUpdates": True,
    "webhookType": 0,
    "partner": "hbturpin",
}

x = requests.post(url, json = json, headers = header)

#print the response text (the content of the requested file):

print(x.text)
