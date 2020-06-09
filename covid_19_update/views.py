from django.shortcuts import render
from django.views import generic
from covid_19_update.models import Author, Genre,User, Articles,Cases,Tweets,Area,Hospital,Pharmacies,Diagramms,SuperMarket
from django.db.models import Sum
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def index(request):
    """View function for home page of site."""

    
    num_Articles11 = Articles.objects.all().count()
    num_Authors = Author.objects.all().count()
    num_Articles=Cases.objects.count()
	
  
   
    
    context = {
        'num_Articles': num_Articles,
        'num_Authors': num_Authors,
    }
    # if not request.user.is_authenticated():
       # return render(request, 'index.html', context=context)
    # # Generate counts of some of the main objects
    # else:
       # return render(request, 'covid.html')

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
	



def show_articles(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Articles = Articles.objects.all().count()
    num_Authors = Author.objects.all().count()
    articles=Articles.objects.all()

  
   
    
    context = {
        'num_Articles': num_Articles,
        'num_Authors': num_Authors,
		'articles': articles
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'test.html', context=context)


def show_tweets(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_tweets = Tweets.objects.all().count()
    tweets=Tweets.objects.all()
    
    for tw in tweets:
       tw.dir=" "
       tw.save()
       tw.dir= dir="../../static/css/"+ tw.img
       tw.save()
  
    

  
   
    
    context = {
        'num_tweets': num_tweets,
        'tweets': tweets,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'tweets.html', context=context)
	
def login(request):

    return render(request, 'login.html')

def covid(request) :
    return render(request,'covid.html')
	
def area_data(request,area_id):
    num_cases=Cases.objects.all().filter(area_id=area_id).count()
    which=Area.objects.filter(pk=area_id)
    pharm=Pharmacies.objects.filter(area_id=area_id)
    name=''
    for wh in which:
       name=wh.Name
	
    
	
   
    context = {
        'num_cases':   num_cases,
        'areas':   name,
		'where':num_cases,
		'pharm':pharm
    }
    return render(request,'pop.html',context=context)