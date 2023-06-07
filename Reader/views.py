from django.shortcuts import render
from .forms import ReaderForm
from django.http import HttpResponseRedirect
# Create your views here.


def redirect(request):
    if request.method == "POST":
        form = ReaderForm(request.post)
        if form.is_valid():
            return HttpResponseRedirect('/book')
    else:
        form = ReaderForm()

    return render(request, "reader_form.html", {"form": form})