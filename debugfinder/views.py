from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'debugfinder/home.html')


def server_status(request):
    return render(request, 'debugfinder/server_status.html')


def login(request):
    context = {
    'Hey there, login successful {user}'
    }
    return render('debugfinder/login.html', context)


def search(request):
    if request.method == 'POST':
        searched = request.get.POST['searched']
        return render(request, 'debugfinder/search.html', searched)
    else:
        return render(request, 'debugfinder/search.html')


def search_results(request):
    return render(request, 'debugfinder/search_results.html')



def docs_index(request):
    return render(request, 'debugfinder/docs_index.html')