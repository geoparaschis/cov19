from django.contrib import admin

# Register your models here.
from .models import Author, Genre,User, Articles,Cases,Tweets,Area,Hospital,Pharmacies,Diagramms,SuperMarket


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Articles)
admin.site.register(User)

admin.site.register(Cases)
admin.site.register(Tweets)
admin.site.register(Area)
admin.site.register(Hospital)
admin.site.register(Pharmacies)
admin.site.register(Diagramms)
admin.site.register(SuperMarket)