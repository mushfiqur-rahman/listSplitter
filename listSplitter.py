import sys, os


print ("""  
 [#] Create By ::
 MUSHFIQ 
                                                   
                             Lists Splitter
""")
	


def run(yList, maxnum, exp):
	sites = open(yList,'r')
	number = 1
	counter = 1
	for site in sites :
		try :
			site = site.strip()
			if counter <= maxnum:
				open('list-'+str(number)+'.txt', 'a').write(site+'\n')
				counter = counter + 1
			else :
				os.system("start cmd /c " + exp + ' list-'+str(number)+'.txt')
				number = number + 1
				open('list-'+str(number)+'.txt', 'a').write(site+'\n')
				counter = 2
		except :
			pass
	os.system("start cmd /c " + exp + ' list-'+str(number)+'.txt')
	print ('\n   ./Done')

yList = str(input('   Your List --> : '))
maxnum = int(input('   maxnummum of every list --> : '))
exp = str(input('   Type any Word --> : '))
run(yList, maxnum, exp)
