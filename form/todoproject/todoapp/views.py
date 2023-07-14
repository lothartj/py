from django.shortcuts import render
from .forms import TodoForm

def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            # Perform any additional actions upon successful form submission
    else:
        form = TodoForm()
        
    return render(request, 'index/index.html', {'model1': form})
