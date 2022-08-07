from django.shortcuts import render

# Create your views here.
def landing_view(requests):
    context = {

    }
    return render(requests, 'index.html', context=context)
def template_page_view(requests):
    context = {

    }
    return render(requests, 'index.html', context=context)
