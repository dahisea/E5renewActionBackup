# -*- coding: UTF-8 -*-
import requests as req
import json, sys, time

# Register an Azure app first; ensure the app has the following permissions:
# Files: Files.Read.All, Files.ReadWrite.All, Sites.Read.All, Sites.ReadWrite.All
# User: User.Read.All, User.ReadWrite.All, Directory.Read.All, Directory.ReadWrite.All
# Mail: Mail.Read, Mail.ReadWrite, MailboxSettings.Read, MailboxSettings.ReadWrite
# After registration, be sure to click the button representing xxx to grant admin consent; otherwise, the Outlook API cannot be invoked.

# Define the file path
path = sys.path[0] + r'/temp.txt'

# Define the function to get the token
def gettoken(refresh_token):
    # Define the request header
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # Define the request parameters
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': id,
        'client_secret': secret,
        'redirect_uri': 'http://localhost:53682/'
    }
    # Send a post request
    html = req.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=data, headers=headers)
    # Parse the response result
    jsontxt = json.loads(html.text)
    # Get the new token
    refresh_token = jsontxt['refresh_token']
    access_token = jsontxt['access_token']
    # Write the new token to the file
    with open(path, 'w+') as f:
        f.write(refresh_token)

# Define the main function
def main():
    # Open the file
    fo = open(path, "r+")
    # Read the file content
    refresh_token = fo.read()
    # Close the file
    fo.close()
    # Call the function to get the token
    gettoken(refresh_token)

# Execute the main function
main()
