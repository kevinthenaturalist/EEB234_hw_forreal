#for pexpect: 
#in python you must first type "import pexpect" after installing in vagrant via shell

newprimates = open("primates2.nex", "w") #currently empty
oldprimates = open("primates.nex").read()
corrected = oldprimates.replace("mcmc", "mcmcp")
corrected.find("mcmcp") #search to confirm replacement
#returns index if found
newprimates.write(corrected) #writes corrected text with mcmcp to primates2.nex

child = pexpect.spawn("mb -i primates2.nex") #-i tells mrbayes to run in interactive mode
#send string "mcmc" to process; tells mrbayes to start running. \r is carriage return

#in shell: chmod u+x primates2.nex

child.sendline(r"mcmc") #returns "5", idk why
child.sendline("no") #returns "3", idk why
child.expect("MrBayes >") #returns "0", idk why
print child.before
#if mrbayes didn't work you'll see there was an "Error in command "Execute"" ...
#if changing to mcmcp apparently must also remove the "sump" and "sumt" args from nexus file?
#can remove by doing as above with .replace("sump;", "")
child.sendline("quit") #quits mrbayes


#homework2
child2 = pexpect.spawn("mb -i")
child2.sendline("execute primates2.nex")
child2.sendline("sumt")
child2.expect("MrBayes >") #check to see that the mrbayes cmd promt is returned
print child.before #print everything before the mrbayes prompt
child2.sendline("sump") #send sump command to mrbayes
child2.sendline("quit")
#how do I know if this all worked successfully? I didn't see a tree result or anything

#can combine glob's listing power with pexpect to automate data analysis,
#e.g. tell mrbayes to analyze all of the nexus files in a folder
import glob, pexpect
nexus_files = glob.glob("*.nex")
for nex in nexus_files:
    output = pexpect.run("mb nex")

#HW3: write func that takes a nexus file and a numgen variable to interactively start mrbayes
##numgen variable = integer that is 1000 or greater; try setting a default if you remember how
#to set a default: def func1(files, ngen=1000): #ngen=1000 sets the default to 1000 for func1
##func should send cmd "set nowarn = yes" to mrbayes
##func should send "mcmcp ngen = XX" where xx is the string of numgen
##func should send cmd "mcmc" to mrbayes
##func should send cmd "no" to mrbayes (do not continue analysis)
##func should send cmd "quit" to mrbayes
#write a 2nd func: takes a nexus file and runs sumt and sump in mrbayes
##add these functions to a script/define them
##once defined, script should:
###print the line "there are XX total files in the current directory and yy files that end in .t"
###call func 1 with primates2.nex
###call func 2 with primates2.nex
###print the line "there are xx total files in the current directory and yy files that end in '.t'"
###print the line "these files end in '.t':" followed by the names of the *.t files, separated by commas
#BONUS: capture stdout of func 2 to a logfile
##then add lines to the end of your script that scrapes the three lines following this output:
###"Credible sets of trees (3 trees sampled):" when sumt is called
###print the number of trees found in each credible interval
import glob, pexpect, re

#for these functions to work: remove mrbayes block from nexus file and make sure no .t/.p/.sum/whatever files exist. Just the nexus - i.e. it hasn't been run previously.
def runbayes(file, ngen=10000):
    child = pexpect.spawn("mb -i " + str(file))
    #child.sendline("set nowarn = yes")
    child.sendline("mcmcp ngen=" + str(ngen))
    child.expect("MrBayes >")
    child.sendline("mcmc")
    child.expect("MrBayes >")
    child.sendline("no")
    child.expect("MrBayes >")
    child.sendline("quit")
def runsum(file):
    logfile = open(str(file) + '.log', 'a')
    child = pexpect.spawn("mb -i " + str(file))
    #child.expect("(yes/no):")
    #child.sendline("yes") #sends command to overwrite old results
    #child.expect("(yes/no):")
    #child.sendline("yes") #sends command to overwrite old results
    child.expect("MrBayes >")
    #logfile.write(child.before)
    child.sendline("sumt")
    child.expect("MrBayes >")
    logfile.write(child.before)
    child.sendline("sump")
    #child.expect("(yes/no):")
    #child.sendline("yes") #sends command to overwrite old results
    #child.expect("(yes/no):")
    #child.sendline("yes") #sends command to overwrite old results
    child.expect("MrBayes >")
    logfile.write(child.before)
    child.sendline("quit") #"no" might work instead of "quit"?
    logfile.close()
    

nexus_files = glob.glob("*.nex")
t_files = glob.glob("*.t")
ngen = #whatever number you want, but default set to 1000
for nex in nexus_files:
    output = runbayes(nex)
    summary = runsum(nex)
print "There are " + str(len(nexus_files)) + " nexus files in the current directory and " + str(len(t_files)) + " files that end in '.t'"
print "These files end in '.t': " + str(t_files).strip('[]')
log4 = open("primates4.nex.log", "r")
log4 = log4.read()
pattern = r"9[059] % credible set contains [0-9]+ trees"
print re.findall(pattern, log4)

