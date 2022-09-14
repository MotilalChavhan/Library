from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from accounts.models import User, Book
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

def student_view(request):
    books = Book.objects.all()
    return render(request, "student_view.html", {
        'books' : books,
    })

@login_required(login_url='account_login')
def create(request):
    if request.method == 'POST':
        new = Book()
        new.user = User.objects.get(pk=request.user.pk)
        new.book_title = request.POST['book_title']
        new.author = request.POST['author']
        new.book_description = request.POST['book_description']
        new.isbn = request.POST['isbn']
        new.pages = request.POST['pages']
        new.save()
        return HttpResponseRedirect(reverse("landing"))
    else:
        return HttpResponseRedirect(reverse("admin_panel"))

@login_required(login_url='account_login')
def admin_panel(request):
    return render(request, "admin_panel.html")
