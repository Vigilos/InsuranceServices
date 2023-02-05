from django.shortcuts import render
from .forms import EmailForm

# def index_view(request):
#     return render(request, "index.html")


def form_view(request):
    if request.POST:
        form = EmailForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print('POST successful!')
    return render(request, 'index.html', {'form': EmailForm})
