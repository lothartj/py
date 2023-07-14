from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoginForm()
    
    return render (request, 'index/index.html', {'forms':form})