from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse




monthly_task = {
    
    "january": "This January",
    "february": "This is February",
    "march": "This is March",
    "april": "This is april",
    "may": "This is may",
    "june": "This is june",
    "july" : "This is july",
    "august": "This is august",
    "september": "This is september",
    "october": "This is ocatober",
    "november": "This is november",
    "december": "This is december"
}
# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_task.keys())
    
    for month in months:
        cap_month = month.capitalize()
        month_path = reverse("task-month", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{cap_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):
    months = list(monthly_task.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>This Month is not supported</h1>")
    forwarded_month = months[month - 1]
    redirected_path = reverse("task-month",args=[forwarded_month])
    
    return HttpResponseRedirect(redirected_path)




def monthly_challenges(request, month):
    try:
        task = monthly_task[month]
        challenge_text =f"<h1>{task}</h1>"
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")