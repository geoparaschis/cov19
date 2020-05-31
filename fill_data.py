import os


os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"



import csv

if __name__ == '__main__':
    print ("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'softeng.settings')
    import django
    django.setup()
    from covid_19_update.models import Author, Genre,User, Articles,Cases,Tweets,Area,Hospital,Pharmacies,Diagramms,SuperMarket
    nomoi=[]
    with open('greece.csv',encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count>0:
               print(row[0])
               pop=row[1]
               case=row[6]
               death=row[8]
               if not pop:
                   pop='0'
               if not case:
                   case='0'
               if not death:
                   death='0'
               nomoi.append((row[0],pop,case,death))
              
                    
            else:
               line_count+=1
            
               
    print('Processed {line_count} lines.')
    for i in range (58):
      a = Area(Name = nomoi[i][0],color='grey',population=int(nomoi[i][1]))
      a.save()
      print(a.Name)
      
      for j in range (int(nomoi[i][2])):
          b=Cases(area_id=a)
          b.save()


