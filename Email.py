import smtplib
from email.message import EmailMessage

def Email(sender,password,receiver,msg_body):
    # action
    msg = EmailMessage()
    msg['subject'] = input("Subject : ")   
    msg['from'] = sender
    msg['to'] = reciever
    msg.set_content(msg_body)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        try:
            smtp.login(sender,password)
            smtp.send_message(msg)
            print("Email sent sucessfully !!")
        except SMTPAuthenticationError:
            print("The username and/or password you entered is incorrect")
        except:
            print("An error occurred")
    

if __name__ == "__main__":
    sender = input("Sender Email Address : ")
    password = input("Sender Password : ")
    receiver = input("Receiver Email Address : ")
    msg_body = input("Message : ")
    
    Email(sender,password,receiver,msg_body)