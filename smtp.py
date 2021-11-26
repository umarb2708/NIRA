import smtplib
import import_file as f

sender_email="hirarobot@gmail.com"
sender_password="Admin@HIRA123#"

def send_email(command):
    str="To whom you want to send"
    f.tts.speak(str)
    person=f.cmd.get_input()
    val=f.db.get_contact(person)
    if (val["found"]):
        receiver_email=val["email"]
        str="What is the message"
        f.tts.speak(str)
        msg=f.cmd.get_input()

        try:
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(sender_email, sender_password)
            mail.sendmail(sender_email, receiver_email, msg)
            mail.close()
            return "Email Success::OK"
        except Exception as e:
            print(e)
            return "Email Failed::FAIL"
    else:
        str=person+" not found. Do you want to add new contact ?"
        f.tts.speak(str)
        reply=f.cmd.get_input()


