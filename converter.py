import csv
import datetime
import argparse


class Converter:

    def __init__(self, file, out):
        self.file = file
        self.out = out

    def convert(self):
        print("Starting Conversion from csv to vcf!")
        try:
            with open(self.file, 'r') as inf:
                with open(self.out, 'w') as outf:
                    data = csv.DictReader(inf)
                    for line in data:
                        write_line(outf, line)
        except FileNotFoundError:
            print("The specified input file %s does not exist" % self.file)
        print("Conversion successful!")


def write_line(file, line):
    init_card(file)
    write_name(file, line['First Name'], line['Last Name'])
    write_birthday(file, line['Birthday'])
    write_phone_mobile(file, line['Mobile Phone'])
    write_phone_home(file, line['Home Phone'])
    write_phone_work(file, line['Business Phone'])
    write_mail(file, line['E-mail Address'], line['E-mail 2 Address'], line['E-mail 3 Address'])
    write_addr_home(file, line['Home Address'])
    write_addr_business(file, line['Business Address'])
    # write_addr(file)
    write_website(file, line['Web Page'])
    end_card(file)


def init_card(file):
    file.write("BEGIN:VCARD\n")
    file.write("VERSION:3.0\n")


def write_name(file, first_name, last_name):
    if first_name:
        file.write("N:" + last_name + ";" + first_name + ";;;" + "\n")
    if last_name:
        file.write("FN:" + first_name + " " + last_name + "\n")


def write_birthday(file, bday):
    if len(bday) > 1:
        bday = datetime.datetime.strptime(bday, "%d.%M.%Y")
        file.write("BDAY:" + bday.strftime('%Y-%M-%d') + "\n")


def write_phone_mobile(file, num):
    if num:
        file.write("TEL;type=CELL:" + num + "\n")


def write_phone_home(file, num):
    if num:
        file.write("TEL;type=HOME:" + num + "\n")


def write_phone_work(file, num):
    if num:
        file.write("TEL;type=WORK:" + num + "\n")


def write_mail(file, mail_home, mail_mobile, mail_work):
    if mail_work:
        file.write("EMAIL;type=INTERNET;type=WORK;type=pref:" + mail_work + "\n")
    if mail_home:
        file.write("EMAIL;type=INTERNET;type=HOME;type=pref:" + mail_home + "\n")
    if mail_mobile:
        file.write("EMAIL;type=INTERNET;type=CELL;type=pref:" + mail_mobile + "\n")


def write_addr_home(file, addr):
    if addr:
        file.write("ADR;TYPE=HOME:;;"+ addr + "\n")


def write_addr_business(file, addr):
    if addr:
        file.write("ADR;TYPE=WORK:;;" + addr + "\n")


def write_website(file, url):
    if url:
        file.write('item3.URL;type=pref:' + url + "\n")


def end_card(file):
    file.write("END:VCARD\n")
