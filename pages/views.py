from django.shortcuts import render,redirect
from .models import Book,Category
from .forms import BookForm

# Create your views here.
def index(request):
    allbook=Book.objects.all()
    allcategory=Category.objects.all()
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:

        form=BookForm()

    context={
        'books':allbook,
        'category':allcategory,
        'form':form

             }
    return render(request,'pages/index.html',context)
