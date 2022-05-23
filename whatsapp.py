#import pywhatkit
#pywhatkit.sendwhatmsg('+918086021791', 'Hurray, I send it ', 23, 00)


from twilio.rest import Client 
 
account_sid = 'ACb900b91b444b5475a8509171e81200a7' 
auth_token = '1f8bf5a9d14cce2c5ba45eb61b6eea70' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',      
                              to='whatsapp:+918086021791' 
                          ) 
 
print(message.sid)
