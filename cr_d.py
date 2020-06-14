# -*- coding: utf-8 -*-

import os


os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
import matplotlib.pyplot as plt


import csv

if __name__ == '__main__':
    print ("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'softeng.settings')
    import django
    django.setup()
    from covid_19_update.models import Author, Genre,User, Articles,Cases,Tweets,Area,Hospital,Pharmacies,Diagramms,SuperMarket,Deaths
    cases=[]
    
    with open('greeceTimeline.csv',encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count>0:
               print(row)


for i in range(0, len(row)): 
    row[i] = float (row[i]) 
plt.plot(row)
plt.title('Κρούσματα από Μάρτη μέχρι σήμερα')
plt.ylabel('Κρούσματα')
plt.xlabel('Ημέρα')
#plt.legend(['Train'], loc='upper left')
plt.show()


with open('deaths.csv',encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
   
    for rr in csv_reader:
        print(rr)

for i in range(0, len(rr)): 
    rr[i] = float (rr[i]) 
deaths=[]          
sum=0
for i in  range (len(rr)):
    sum=rr[i]+sum
    deaths.append(sum)         
    
plt.plot(deaths)
plt.title('Θάνατοι από Μάρτη μέχρι σήμερα')
plt.ylabel('Θάνατοι')
plt.xlabel('Ημέρα')
#plt.legend(['Train'], loc='upper left')
plt.show()
