from django.shortcuts import render
from testapp.models import  Book
from django.views.generic import ListView,DetailView
# Create your views here.
def info(request):
    books=Book.objects.all()
    return render(request,'testapp/info.html',{'books':books})

class BookListView(ListView):
    model=Book
    template_name='testapp/books.html'
    context_object_name='list_of_bookd'

class bookDetailview(DetailView):
    model=Book
