
# -*- coding: utf-8 -*-
#authentication is handled here
from __future__ import unicode_literals
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import UserLoginForm
from listcustomers.views import index

# the login_view authenticates credentials the user inputs and redirects them to the listcustomers page
def login_view(request):
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())

        return redirect('/listcustomers')

    return render(request, "accounts/form.html", {"title": title, "form":form})


#logout method

def logout_view(request):
    logout(request)
    return redirect('login')
