#Kevin Neal
#EEB 234 homework, February 17

from bs4 import BeautifulSoup
import re

for num in range(1, 800):
    inputfile = str(num) + ".html"
    html = BeautifulSoup(open(inputfile))
    if str(html).find("EcoEvoPub Series") == -1:
        print("")
    else:
        section = html.find(class_="section")
       # date = str(section.find("h4").string.strip()) #this keeps failing
        date = str(re.findall(r"[A-Za-z]{3,9}\s\d\d?\s\d{4}", str(section))).strip() #might not work
	names = re.findall(r"[A-Z]+\s[A-Z]*\.?\s*[A-Z]+", str(section))
        if len(names) == 2:
            name1 = str(names[0])
            name2 = str(names[1])
            print("EcoEvoPub, " + date + ": " + name1 + " and " + name2 + " presenting")
        elif len(names) == 1:
            name1 = str(names[0])
            print("EcoEvoPub, " + date + ": " + name1 + " presenting")
        else:
            print("")

#I was basing this code off of the html of 797.html; only works for some
#of the pages since 2011 because formatting has changed across files.
#Not clear how to generalize.
