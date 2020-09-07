import pandas as pd
import smtplib
a = pd.read_excel("Email.xlsx")
emails = a['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("<SenderAddress>", "<password>")
msg = "Hello this is a broadcast email using python"
subject = "Hello wwlcome to the world of python"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
