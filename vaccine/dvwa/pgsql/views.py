from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import GetUserForm
from .models import User

# Low
# $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
# Meduim
# $query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
# High
# $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";

def index(request):
    all_users = []
    if request.method == "GET":
        form = GetUserForm(request.GET)
        if form.is_valid():
            all_users = User.objects.all()
            print(all_users)
    return render(request, "pgsql/display.html", {"users": all_users})