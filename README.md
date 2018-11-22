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
- call the main method via the commandline
- if no args are provided the gui will appear
- if you do not want a gui, just pass the following args, replacing <contacts> with the acutal names
- -in <contacts>.csv
- -out <contacts>.vcf
