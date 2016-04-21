from __future__ import print_function
import httplib2
import os
from apiclient import errors
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from email.mime.text import MIMEText
import base64
from django.conf import settings



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCOPES = 'https://www.googleapis.com/auth/gmail.compose'
CLIENT_SECRET_FILE = os.path.join(BASE_DIR,'client_secret.json')


def get_credentials():
    credential_path = os.path.join(BASE_DIR, 'gmail.storage')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
     
        credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials



# create a message to send

def send(to, subject, message_text):
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('gmail', 'v1', http=http)
	message = MIMEText(message_text)
	message['to'] = to
	message['from'] = settings.GMAIL_FROM_EMAIL
	message['subject'] = subject
	body =  {'raw': base64.urlsafe_b64encode(message.as_string())}


	try:
		message = (service.users().messages().send(userId="me", body=body).execute())
	except errors.HttpError, error:
		print (error)
	return