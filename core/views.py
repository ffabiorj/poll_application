from django.shortcuts import render, redirect, get_object_or_404
from core.models import Poll
from django.http import HttpResponse

from core.forms import CreatePollForm


def home(request):
    polls = Poll.objects.all()
    context = {"polls": polls}
    return render(request, "poll/index.html", context)


def create(request):
    if request.method == "POST":
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreatePollForm()
    form = CreatePollForm()
    context = {"form": form}
    return render(request, "poll/create.html", context)


def vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == "POST":
        selected = request.POST["poll"]
        # import ipdb; ipdb.set_trace()
        if selected == "option1":
            poll.option_one_count += 1
        elif selected == "option2":
            poll.option_two_count += 1
        elif selected == "option3":
            poll.option_three_count += 1
        else:
            return HttpResponse(200, "Invalid form")

        poll.save()

        return redirect("result", poll.id)

    context = {"poll": poll}
    return render(request, "poll/vote.html", context)


def result(request, pk):
    poll = Poll.objects.get(pk=pk)
    context = {"poll": poll}
    return render(request, "poll/result.html", context)
