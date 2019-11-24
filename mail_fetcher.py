from imaplib import IMAP4_SSL
import email
import os
import json
import actions


search = json.load(open('search_actions.json','r'))

print(search['email'])

def process_message(mail,action):

    actions.opt[action](mail)


#connect and login to the mailserver
try:
    mailserver = IMAP4_SSL(environ['server'])
    resp = mailserver.login(environ['user'],environ['passwd'])
except imaplib.error as err:
    print(err)
    print("unable to login or connect to server.")

#select the inbox 'folder'
mailserver.select("INBOX")

for option in search['email']:
    print(option)

    (repcode, list) = mailserver.uid('search', None, '(%s)' % option['search-criteria'])
    print(list)
    if len(list[0].decode('utf-8')) == 0:
        break
    else:
        messages = list[0].decode('utf-8').split(' ')
        
        for message in messages:
            (repcode,data) = mailserver.fetch(message, 'RFC822')
            raw_data = data[0][1].decode('utf-8')
            msg = email.message_from_string(raw_data)
            
            print(option['actions'])
            process_message(msg,option['actions'])
             
            
