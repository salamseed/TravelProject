from django.shortcuts import render
from . models import whychooseus
from . models import meet_the_team
def displayweb(request):
    item1=whychooseus.objects.all()
    item2=meet_the_team.objects.all()
    return  render(request,'index.html',{'obj':item1,'obj1':item2})

