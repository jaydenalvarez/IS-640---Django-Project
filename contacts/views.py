from django.shortcuts import render

def start_page(request):
    return render(request, 'contacts/start_page.html')