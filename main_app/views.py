from django.shortcuts import render
from .models import Newsletter
from .forms import NewsletterSignUpForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignUpForm(request.POST or None)
        if form.is_valid():
            user = Newsletter(
                first_name = request.POST['first_name'],
                email = request.POST['email'],
            )
            user.save()
            context = {
                'form': form,
            }
            return render(request, 'home.html', context)
        else:
            print('Form not valid')
    else:
        form = NewsletterSignUpForm(request.POST or None)
        context = {
                'form': form,
            }
    return render(request, 'home.html', context)

def newsletter_unsubscribe(request):
    form = NewsletterSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Newsletter.objects.filter(email = instance.email).exist():
            Newsletter.objects.filter(email = instance.email).delete()
        else: 
            print("Email doesn't exist")


    context = {
        'form': form,
    }

    template = "newsletters/unsubscribe.html"
    return render(request, template, context)

def mobile(request):
    if request.method == 'POST':
        form = NewsletterSignUpForm(request.POST or None)
        if form.is_valid():
            user = Newsletter(
                first_name = request.POST['first_name'],
                email = request.POST['email'],
            )
            user.save()
            context = {
                'form': form,
            }
            return render(request, 'mobile.html', context)
        else:
            print('Form not valid')
    else:
        form = NewsletterSignUpForm(request.POST or None)
        context = {
                'form': form,
            }
    return render(request, 'mobile.html', context)
