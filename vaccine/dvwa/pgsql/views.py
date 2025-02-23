from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from .models import User

# Low
# $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
# Meduim
# $query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
# High
# $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";

def index(request):
    users_count = User.objects.count()
    users = []
    form = UserForm()
    if request.method == "GET":
        form = UserForm(request.GET)
        if form.is_valid():
            id = form['id'].value()
            query  = f"SELECT * FROM {User.__table_name__} WHERE id = '{id}'"
            users = User.objects.raw(query)
    return render(request, "pgsql/display.html", {"form": form, "users_count": users_count, "users": users})

def login(request):
    form = LoginForm()
    error_message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = form['username'].value()
        password = form['password'].value()
        query  = f"SELECT * FROM {User.__table_name__} WHERE username = '{username}' and password = '{password}' LIMIT 1"
        users = User.objects.raw(query)
        if users:
            print('users:', users)
            return redirect('/pgsql')
        else:
            error_message = "user or password not correct"
    return render(request, "pgsql/login.html", { 'form': form, "error_message": error_message })