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
    users_count = User.objects.count()
    if request.method == "GET":
        form = GetUserForm(request.GET)
        if form.is_valid():
            id = form['user_id'].value()
            query  = f"SELECT * FROM users WHERE id = {id}"
            users = User.objects.raw(query)
            for u in users:
                print(u)
    return render(request, "pgsql/display.html", {"form": form, "users_count": users_count, "users": users})