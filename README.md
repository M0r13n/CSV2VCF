# CSV2VCF
Python Script for converting .csv contact files to .vcf. 

This script is handy if you need to transfer contacts from a phone running windows to a new android/ iOS device. 

# IMPORTANT

I assume no liability for the use of my program. Use at your own Risk. Data loss or corrupted data can occur.
If you find a bug or want to contribute new features, feel free to create a pull request.

Currently the following information will be converted:
- Name (Firstname, Lastname)
- Birthday
- Numbers (mobile, home, work)
- Mail (mobile, home, work)
- Address (home, work)
- Website


# Usage
- make sure you have Python3 installed
- clone this repo
- make sure this script and the target .csv file are in the same directory
- open a console and type, while replacing contacts.csv with the actual name of the target file: "python converter.py -in contacts.csv"
- if everthing worked you can see a new file named "contacts.vcf" in the same directory,
