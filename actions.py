import os
#import libraries needed to process the actions

#print the body of the message and that's it
def print_body(msg):
    
    for part in msg.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))

        if ctype == 'text/plain' and 'attachment' not in cdispo:
            print(part.get_payload(decode=True))
            break

#save the attachment to the filesystem
def text(msg):

    #DEFINE LOCATION FOR FILE
    filePath = os.getcwd()
    
    for part in msg.walk():
        cdispo = str(part.get('Content-Disposition'))
        
        if part.get_content_maintype() == 'multipart':
            continue
        
        if "attachment" in cdispo:
            fileName = part.get_filename()
            file = open(os.path.join(filePath,fileName), 'wb')
            file.write(part.get_payload(decode=True))
            file.close
            
            print('file saved to %s/%s' % (filePath, fileName))
            
# save to an excel file and manipulate data          
def excel(msg):
    #use text() to save the file
    text(msg)

# map the inputs to the function blocks
opt = {"print body" : print_body,
           "text attachment save" : text,
           "spreadsheet attachment" : excel,
}
