from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Quote
from .forms import QuoteForm

def quote_list(request):
    quotes = Quote.objects.all().order_by('-created_at')
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.created_by = request.user
            quote.save()
            return redirect('quote_list')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})
