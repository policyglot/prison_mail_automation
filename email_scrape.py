from login import email_id, password
import email, getpass, imaplib, os, re
import matplotlib.pyplot as plt

user = raw_input("Enter your GMail username --> ")
pwd = getpass.getpass("Enter your password --> ")

m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user, pwd)
m.list()