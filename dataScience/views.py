from django.shortcuts import render

# Create your views here.

def homeds(request):
    context = {
        'first_name': 'Rafe',
        'last_name': 'Stefano',
        'my_list': [1,4,6,88,3,5]
    }
    return render(request,'dataScience/index.html',context)