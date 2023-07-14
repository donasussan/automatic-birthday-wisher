Pass_word = ""
import random
import pandas
import datetime
import smtplib

today = datetime.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today.month, today.day]

    file_path = f"letters/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        letter = contents.replace("[NAME]", birthday_person["name"])
        email_to = birthday_person["email"]
    # send email.

    my_email = 'donasussanchacko@gmail.com'
    password = Pass_word
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email_to,
        msg=f"Subject: Happy Birthday\n\n {letter}")
    connection.close()

# we are collecting the datas from the csv file. data_row is a pandas operation to fetch the
# data of a particular row. Month and day is passed as tuples to get details
# of the user like name and email and is stored in a dictionary

# if the today tuple is present in the dictionary we should collect that information,
# birthday person gives the info of the passed key i.e today tuple olla aalde baaki details
# make changes in the Name in the letter.
# to replace, specify content to replace with the original value to be kept.
# birthday_dict = {   (birthmonth, birthday): dona@gmail.com, 2000,02,15} #the key is a tuple
