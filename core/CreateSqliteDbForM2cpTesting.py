import sqlite3
from logzero import logger

db_location = './TestSuiteDatabase.db'

msg = "Creating database at {}".format(db_location)
logger.info(msg)

conn = sqlite3.connect(db_location)
c = conn.cursor()

c.execute("PRAGMA foreign_keys = ON;")

c.execute('''CREATE TABLE Test(Name TEXT PRIMARY KEY, Description TEXT)''')

c.execute('''CREATE TABLE TestDefinition(TestName TEXT, VersionNumber INTEGER, RobotCode TEXT, Comment TEXT,
             PRIMARY KEY(TestName, VersionNumber), FOREIGN KEY(TestName) REFERENCES Test(Name))''')

c.execute('''CREATE TABLE TestParameterDependency(TestName TEXT, TestVersionNumber INTEGER, ParameterDomain TEXT, ParameterName TEXT, ParameterVersion INTEGER, 
            CONSTRAINT unq UNIQUE(TestName, TestVersionNumber, ParameterName), 
            FOREIGN KEY(TestName, TestVersionNumber) REFERENCES TestDefinition(TestName, VersionNumber), 
            FOREIGN KEY(ParameterDomain, ParameterName, ParameterVersion) REFERENCES Parameter(Domain, Name, Version))''')

c.execute('''CREATE TABLE Parameter(Domain TEXT, Name TEXT, Version INTEGER, Data TEXT, PRIMARY KEY(Domain, Name, Version))''')

conn.commit()
conn.close()

msg = "...done!"
logger.info(msg)