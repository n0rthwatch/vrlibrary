from datetime import date
from django.utils.text import slugify
from librarySite.models import Book, Author, Genre
import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
application = get_wsgi_application()

for book in book_data:
    title, pages_count, downloads_count, description, created_at, author_name, image_path, genre_names = book

    # create or get the author
    author_slug = slugify(author_name)
    author, created = Author.objects.get_or_create(name=author_name, defaults={'slug': author_slug})

    # create the book
    book_slug = slugify(title)
    book = Book.objects.create(title=title, slug=book_slug, pages_count=pages_count, downloads_count=downloads_count,
                               description=description, created_at=date.fromisoformat(created_at), author=author,
                               image=image_path)

    # add genres to the book
    for genre_name in genre_names:
        genre, created = Genre.objects.get_or_create(name=genre_name)
        book.genre.add(genre)

print('Finished populating the database with book data.')
