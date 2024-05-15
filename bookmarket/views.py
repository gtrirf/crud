from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddReviewForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Books, Review
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.edit import UpdateView
from .forms import BookForm
from django.contrib import messages


class BookListView(View):
    def get(self, request):
        book = Books.objects.all().order_by('-id')
        context = {
            'book': book
        }
        return render(request, 'book_list.html', context=context )


class BookDetailView(View):
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        reviews = Review.objects.filter(book=pk)
        context = {
            'book': book,
            'reviews': reviews
        }
        return render(request, 'book_detail.html', context=context)


# class BookUpdateView(UpdateView):
#     model = Books  # Specify the model
#     fields = ['title', 'description', 'price', 'image']
#     template_name = 'update.html'
#


class BookUpdateView(View):
    def get(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        form = BookForm(instance=book)
        return render(request, 'update.html', {'form': form})

    def post(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:book_detail', pk=pk)
        else:
            return render(request, 'update.html', {'form': form})


class BookCreateView(CreateView):
    model = Books
    template_name = 'book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('books:book_list')


class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book_delete.html'
    success_url = reverse_lazy('books:book_list')


class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        books = Books.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'books': books,
            'add_review_form': add_review_form
        }
        return render(request, 'add_review.html', context=context)

    def post(self, request, pk):
        books = Books.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                book=books,
                user=request.user,
                star_given=add_review_form.cleaned_data['star_given']
            )

            review.save()
            return redirect('books:book_detail', pk=pk)
        else:
            messages.error(request, 'Failed to add review. Please check the form.')
            return render(request, 'add_review.html', {'books': books, 'add_review_form': add_review_form})