import smtplib
import datetime as dt
import random

my_email = "donasussan2k@gmail.com"
password = "kmunkemxzfjbdpwa"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="donasussan2000@gmail.com",
    msg="Subject:  This is a test email\n\n My test email")
connection.close()
# Creating a date time module
now = dt.datetime.now()
year = now.year
month = now.month
week_day = now.weekday()

# Motivational quote for Mondays


if week_day == 2:
    with open('quotes.txt', 'r') as file:
        lines = file.readlines()
        quote = random.choice(lines)
    print(quote)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="donasussan2000@gmail.com", msg=f'Subject:Monday Motivation\n\n{quote}')

# Birthday - new date time object
date_of_birth = dt.datetime(year=2000, month=2, day=15)
print(date_of_birth)


