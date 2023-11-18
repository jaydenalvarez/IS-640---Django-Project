from django.shortcuts import render, redirect
from .forms import ContactForm

def start_page(request):
    return render(request, 'contacts/start_page.html')

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start_page')
    else:
        form = ContactForm()
    
    return render(request, 'contacts/create_contact.html', {'form': form})