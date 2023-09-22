import os
from datetime import date,time,datetime
date=date.today()
time=datetime.now()
name=(str(date)+" SIYA_VA_DIARY.txt")
logger = open(name,"a+")
logger.write(str(time)[11]+str(time)[12]+":"+str(time)[14]+str(time)[15]+"\n")
logger.close()
