# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:57:25 2020

@author: dalas
"""

import os


os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"



import csv

if __name__ == '__main__':
    print ("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'softeng.settings')
    import django
    django.setup()
    from covid_19_update.models import Author, Genre,User, Articles,Cases,Tweets,Area,Hospital,Pharmacies,Diagramms,SuperMarket,Deaths
    cases=[]
    deaths=[]
    with open('greeceTimeline.csv',encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count>0:
               print(row)
         