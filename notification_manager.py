import smtplib

EMAIL = "nalinpython@gmail.com"
PASSWORD = "Nalingmail@7"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def mail(self, message):
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.starttls()
        mail.login(EMAIL, PASSWORD)
        mail.sendmail(from_addr=EMAIL,
                      to_addrs="nalinkaushik7@yahoo.com",
                      msg=message)
