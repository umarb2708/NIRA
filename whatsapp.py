#import pywhatkit
#pywhatkit.sendwhatmsg('+918086021791', 'Hurray, I send it ', 23, 00)

import import_file as f
from twilio.rest import Client 
 
account_sid = 'ACb900b91b444b5475a8509171e81200a7' 
auth_token = '5d2f71311593231d70d30ae91fa60f99' 
client = Client(account_sid, auth_token) 
 
def get_person(command):
    person="umar"
    #function to find person in query or input
    if 'to' in command:
        split_c=command.split('to')
        person=split_c[1].replace("\n","")
    else:
        say="To whom you want to send mail"
        f.out.txt_out(say,'100')
        person=f.inp.get_cmd("receiver")

    return person 



def whatsapp(command):
    person=get_person(command)
    val=f.db.get_contact(person)
    if (val["found"]):
        to=val["phone"]
        say="What is the message"
        f.out.txt_out(say,'100')
        msg=f.inp.get_cmd("Message")
        message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=msg,      
                              to='whatsapp:+91'+to 
                          )
        #print(message.sid)
        return 1
    else:
        say="No contact found. Kindly add"
        f.out.txt_out(say,'100')

        return 0

