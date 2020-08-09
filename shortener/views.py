from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DashboardForm
from .models import *
import random
import string


# Create your views here.


def home(request, query=None):
    if not query or query is None:
        return render(request, 'shortener/home.html')
    else:
        try:
            check = URLS.objects.get(short_url=query)
            url_to_redirect = check.long_url
            return redirect(url_to_redirect)
        except URLS.DoesNotExist:
            return render(request, 'shortener/home.html', {'error':'error'})


@login_required
def dashboard(request, pk):
    person = Person.objects.get(id=pk)
    myurls = URLS.objects.filter(created_by_id=pk)
    context = {'Person': person, 'myurls': myurls}
    return render(request, 'shortener/dashboard.html', context)


@login_required
def edit(request, pk):
    person = Person.objects.get(id=pk)
    form = DashboardForm(instance=person)

    if request.method == 'POST':
        form = DashboardForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'shortener/dashboard_Edit.html', context)


def randomgen():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))


@login_required()
def generate(request):
    if request.method == "POST":
        # generate
        if request.POST['original'] and request.POST['short']:
            # generate based on user input
            usr = request.user
            original = request.POST['original']
            short = request.POST['short']
            check = URLS.objects.filter(short_url=short)
            if not check:
                newurl = URLS(
                    created_by=usr,
                    long_url=original,
                    short_url=short,
                )
                newurl.save()
                return redirect('/')
            else:
                messages.error(request, "Already Exists")
                return redirect('/')

        elif request.POST['original']:
            # generate randomly
            usr = request.user
            original = request.POST['original']
            generated = False
            while not generated:
                short = randomgen()
                check = URLS.objects.filter(short_url=short)
                if not check:
                    newurl = URLS(
                        created_by=usr,
                        long_url=original,
                        short_url=short,
                    )
                    newurl.save()
                    return redirect('/')
                else:
                    continue
        else:
            messages.error(request, "Empty Fields")
            return redirect('/')
    else:
        return render(request, 'shortener/url_form.html')
