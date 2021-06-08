import requests

#https://humblebundlenotifications.azurewebsites.net/api/RegisterWebhook
#https://humblebundlenotifications.azurewebsites.net/api/TestWebhook
url = 'https://humblebundlenotifications.azurewebsites.net/api/TestWebhook'
header = {"Content-Type": "application/json"}
json = {
    "type": 0,
    "webhook": "",
    "sendUpdates": True,
    "webhookType": 0,
    "partner": "hbturpin",
}

x = requests.post(url, json = json, headers = header)

#print the response text (the content of the requested file):

print(x.text)
