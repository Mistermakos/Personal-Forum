with open("../mail_message.txt") as text:
    message = text.read()
#If you want to change message you have to reset. 
#It's faster this way

print(message)

def notify_users(postTitle: str):
    #get mails of all users
    # send mail, but remember to replace {TITLE} in mail_message.txt file with postTitle
    return True

def send_message(message: str):
    #get mails of all users
    # send mail, but with message as message variable
    return True

