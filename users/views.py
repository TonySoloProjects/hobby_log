"""
user django views to allow users to create and log into their accounts.

Created by: Tony Held tony.held@gmail.com
Created on: 2021/04/18
Copyright © 2021 Tony Held.  All rights reserved.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Register new user."""
    if request.method != 'POST':
        # Display blank for
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('hobby:view_topics')

    # Display blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
