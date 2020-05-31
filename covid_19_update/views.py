from django.shortcuts import render
from django.views import generic
from covid_19_update.models import Author, Genre,User, Articles,Cases,Tweets,Area,Hospital,Pharmacies,Diagramms,SuperMarket
from django.db.models import Sum

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Articles11 = Articles.objects.all().count()
    num_Authors = Author.objects.all().count()
    num_Articles=Cases.objects.filter(area_id='Zakynthos').count()
  
   
    
    context = {
        'num_Articles': num_Articles,
        'num_Authors': num_Authors,
    }

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
    num_Articles = Articles.objects.all().count()+30300303
    num_Authors = Author.objects.all().count()
    

  
   
    
    context = {
        'num_Articles': num_Articles,
        'num_Authors': num_Authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'tweets.html', context=context)
	
def login(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Articles = Articles.objects.all().count()+47324534573583300303
    num_Authors = Author.objects.all().count()
    

  
   
    
    context = {
        'num_Articles': num_Articles,
        'num_Authors': num_Authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'login.html', context=context)
