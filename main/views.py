from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406435585',
        'name': 'Aisyah Saajidah',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)