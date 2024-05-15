from django.shortcuts import render

# Create your views here.
def index(request):

    name = 'Smwinde'


    context =dict(name=name)
    return render(request, 'base/index.html',context=context)
