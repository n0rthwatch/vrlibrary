from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from .forms import *
from .models import *


def index(request):
    books = Book.objects.all()[:4]
    popular = Book.objects.all().order_by('-downloads_count')[:4]
    new = Book.objects.all().order_by('-created_at')[:4]
    news_feed = News.objects.all().order_by('-date')[:4]
    return render(request, 'library/index.html',
                  {
                      'books': books,
                      'popular': popular,
                      'new': new,
                      'news_feed': news_feed
                  })


def profile(request):
    user_profile = request.user.profile
    favorite_books = user_profile.favorite_books.all()
    context = {
        'favorite_books': favorite_books,
    }
    return render(request, 'library/profile_page.html', context)


def news(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'library/news.html', {'news': news})


def add_favorite(request, book_id):
    if request.method == "POST":
        user = request.user
        book = get_object_or_404(Book, id=book_id)
        profile, created = Profile.objects.get_or_create(user=user)
        new_favorite = Like.objects.create(user=user, book=book, alreadyFavorited=True)
        book.favorites += 1
        book.user_favorites.add(profile)
        book.save()
        new_favorite.save()

        messages.success(request, f'Книга "{book.title}" добавлена в избранное')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_favorite(request, book_id):
    if request.method == "POST":
        # retrieve the user's profile
        profile = get_object_or_404(Profile, user=request.user)
        # retrieve the book to be un-favorited
        book = get_object_or_404(Book, id=book_id)

        # remove the favorite
        favorite = Like.objects.filter(user=profile.user, book=book).first()
        if favorite:
            favorite.delete()

            # remove the book from the user's favorites
            book.user_favorites.remove(profile)
            book.favorites -= 1
            book.save()

            messages.success(request, f'Книга "{book.title}" теперь не в избранном')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'library/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username.title()}!')
                return redirect('books')

        messages.error(request, f'Invalid username or password')
        return render(request, 'library/login.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f'Успешный выход из аккаунта.')
    return redirect('/')


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'library/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('books')
        else:
            return render(request, 'library/register.html', {'form': form})


def search(request):
    global query
    if request.GET.get('query'):
        query = request.GET.get('query')
        books = Book.objects.filter(
            Q(title__iregex=query) |
            Q(author__name__iregex=query) |
            Q(description__iregex=query)
        )
    elif request.GET.get('genre'):
        query = request.GET.get('genre')
        books = Book.objects.filter(
            Q(genre__name__iregex=query)
        )
    else:
        books = 0
    return render(request, 'library/search_results.html', {'books': books, 'query': query})


def search_genres(request):
    query = request.GET.get('query')
    if query:
        books = Book.objects.filter(
            Q(genre__name__iregex=query)
        )
    else:
        books = 0
    return render(request, 'library/search_results.html', {'books': books, 'query': query})


class BookListView(generic.ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books_list'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        return context

    def get_ordering(self):
        ordering = self.request.GET.get('order_by')
        return ordering


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_list"] = Book.objects.order_by("-downloads_count")[:4]
        return context
