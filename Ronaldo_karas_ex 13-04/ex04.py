print("=" *50)

email_spam = "fulano@gmail.com, beltrano@gmail.com, ciclano@gmail.com"

email = input("DIGITE SEU E-MAIL: ").lower().strip()

if email in email_spam:
    print("E-MAIL SPAM")
else: 
    print("NÃO É SPAM!")