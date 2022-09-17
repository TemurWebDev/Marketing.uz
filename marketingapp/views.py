from django.shortcuts import render,redirect,reverse
from .models import Bizning_taklif,Biz_kimmiz,Contact,Slaidshow
from .forms import ContactForm

# Create your views here.

def home_view(request):
    slaid = Slaidshow.objects.all()
    taklif = Bizning_taklif.objects.all()
    about = Biz_kimmiz.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = Contact(**form.cleaned_data)
            contact.save()
            return redirect(reverse('home_url'))
    return render(request,'home.html',{'slaids':slaid,'taklif':taklif,'abouts':about,'form':form})



def contact_view(request):
    contact = Contact.objects.all()

    return render(request,'contact.html',{'contacts':contact})