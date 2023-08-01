from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "This is january",
    "february": "This is february",
    "march": "This is march",
    "april": "This is april",
    "may": "This is may",
    "june": "This is june",
    "july": "This is july",
    "august": "This is august",
    "september": "This is september",
    "october": "This is october",
    "november": "This is november",
    "december": None,
}


def home(request):
    months = list(monthly_challenges.keys())
    context = {"months": months}
    return render(request, "challenges/home.html", context)


def month_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    challenge_text = None
    try:
        challenge_text = monthly_challenges[month]
        context = {"challenge": challenge_text, "month": month.capitalize()}
        return render(request, "challenges/challenge.html", context)
    except:
        return HttpResponseNotFound("<h1>Invalid month!</h1>")
