from django.shortcuts import render

# Create your views here.

# function
def landing(request):
    
    return render(request, 
                  template_name='single_pages/landing.html'
                  )

def about(request):
    
    return render(request, 
                  template_name='single_pages/about.html'
                  )