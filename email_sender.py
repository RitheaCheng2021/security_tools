#!/usr/bin/env python
# simple email sender using python
# Author: Rithea
# Date: 16/07/2021
# Please do not use this for spam sender. This is for education purpose only.

import smtplib

print("\n***Please Note: The email might go into receiver spam depend on allow less secure app setting. The sender need to turn on allow less secure app in order to make this script work.\n")
print("***How to turn on/off allow less secure app:")
print("Go to top right corner of webpage> Manage your Google Account> Security> Less secure app access> Turn on/off\n")

sender = input("Your Email: ")
password = input("Your Password: ")
receiver = input("Receiver Email: ")
message = input("Your Message: ")

# port 465 for SMTPS & port 587 for MSA & port 25 for SMTP (Google)
try:
    # can change smtp server and port to use different mail provider
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.starttls()
    mailserver.login(sender, password)
    mailserver.sendmail(sender, receiver, message)
    mailserver.quit()
    print("\nEmail has been sent to", receiver)
except:
    print("\nSorry, something went wrong. \nPlease check your email or password.")
