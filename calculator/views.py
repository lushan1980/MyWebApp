from django.shortcuts import render

# Create your views here.
def calc_view(request):

    return render(request, 'calculator/calc.html')