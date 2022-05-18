import smtplib, ssl
import import_file as f

sender_email="hirarobot@innovize.in"
sender_password="Hira@IES123#"
smtp_link="server61.secureclouddns.net"
port=465
context = ssl.create_default_context()

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
        



def send_email(command):
    person=get_person(command)
    val=f.db.get_contact(person)
    if (val["found"]):
        receiver_email=val["email"]
        say="What is the message"
        f.out.txt_out(say,'100')
        msg=f.inp.get_cmd("Message")

        try:
            mail = smtplib.SMTP_SSL(smtp_link, port , context=context)
            mail.ehlo()
            mail.starttls()
            mail.login(sender_email, sender_password)
            mail.sendmail(sender_email, receiver_email, msg)
            mail.close()
            f.db.insert_cmd_executed("send mail","1")
        except Exception as e:
            #print(e)
            f.db.insert_cmd_executed("send mail","0")
    else:
        str=person+" not found. Do you want to add new contact ?"
        f.tts.speak(str)
        reply=f.inp.get_cmd("Yes/No")
    return 1

