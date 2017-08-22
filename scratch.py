import MySQLdb
import getpass
db=MySQLdb.connect(passwd=getpass.getpass(), db="fullcast2")
c=db.cursor()
c2=db.cursor()
c.execute('SHOW tables from fullcast2')
tables=c.fetchall()
for table in tables:
	print(table[0])
	temp=table[0]
	c2.execute('DESCRIBE %s' % (temp))
	columns=c2.fetchall()
	for column in columns:
		print (column[0])
		print ('   ' + column[1])
	print '\n'

#for each table: retrieve the output of the describe table command, then for each row in that list of rows, print the column name and column type 

# useful tools: string replacement

# useful tool #2: executing SQL with parameters THIS IS ONLY GOOD FOR PYTHON SQL CURSOR COMMANDS
#tablename = "Accounts"
#c.execute('DESCRIBE %s' % (tablename)) 
#print(c.fetchall()) 
