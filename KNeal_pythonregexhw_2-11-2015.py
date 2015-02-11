#code for Python for Biologists exercise, chapter 7 regular expressions
#Kevin Neal

import re
#when using regex must use re.whatever, e.g. re.search(pattern, string)
# \n means start new line, \t means insert tab
# in python: to print special characters you print them "raw":
# print(r"\t\n") will print "\t\n"; the r"" indicates "raw" notation - ignoring Python's internal special characters (but regex will still work!)

#example of searching for a pattern in a string
# dna = "ATCGCATTGAG"
#if re.search(r"GAATTC", dna):
	#print("restriction site found!")
	
#re.findall returns a list
#re.finditer returns the individual strings of all matches of a regex search
#dna = "AGTCGATAGTAGCTA"
#runs = re.finditer(r"[AT]{3,100}", dna)
#for match in runs:
	#run_start = match.start()
	#run_end = match.end()
	#print("AT rich region from " + str(run_start) + " to " + str(run_end)
	
#Accession names:
import re
accessions = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]
#contains the number 5
for contain5 in accessions:
	if re.search(r"5", contain5):
		print contain5

for containde in accessions:
	if re.search(r"([de]", containde):
		print containde
		
for containdeinorder in accessions:
	if re.search(r"d.*e", containdeinorder):
		print containdeinorder
		
for criterion4 in accessions:
	if re.search(r"d.e", criterion4):
		print criterion4
	
for criterion5 in accessions:
	if re.search(r"d.*e", criterion5) or re.search(r"e.*d", criterion5)
		print criterion5

for criterion6 in accessions:
	if criterion6.startswith("x") or criterion6.startswith("y"): #re.search(r"^[xy]", criterion6) also works
		print criterion6
		
for criterion7 in accessions:
	if re.search(r"^[xy]", criterion7) and re.search(r"e^", criterion7):
		print criterion7
		
for criterion8 in accessions:
	if re.search(r"\d{3}", criterion8):
		print criterion8
		
for criterion9 in accessions:
	if re.search(r"d[arp]$", criterion9):
		print criterion9
		

