"""
Hobby django views to allow users to create hobby topics and journal
log entries associated with their favorite hobbies.

Created by: Tony Held tony.held@gmail.com
Created on: 2021/04/18
Copyright © 2021 Tony Held.  All rights reserved.
"""


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    print(f'in index()')
    return render(request, "hobby/index.html")

@login_required
def view_topics(request):
    print(f'in view_topics()')
    # queryset = Topic.objects.all()
    # queryset = Topic.objects.order_by('date_added')
    queryset = Topic.objects.filter(owner=request.user).order_by('date_added')

    context = {
        "topics": queryset
    }
    return render(request, "hobby/topics.html", context)

@login_required
def view_topic(request, topic_id):
    print(f'in view_topic()')

    # topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')

    context = {
        "topic": topic,
        "entries": entries
    }
    return render(request, "hobby/topic.html", context)

@login_required
def delete_topic(request, topic_id):
    print(f'in delete_topic()')

    # topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)

    if topic.owner != request.user:
        raise Http404

    if request.method == 'POST':
        # Delete the topic if from a valid post form
        topic.delete()
        return redirect('hobby:view_topics')

    context = {
        'topic': topic
    }

    return render(request, "hobby/delete_topic.html", context)


@login_required
def create_topic(request):
    print(f'in create_topic()')
    print(f'{request.method=}')

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('hobby:view_topics')
        else:
            print('form not valid')
    else:
        # No form data submitted, so create the form
        form = TopicForm()

    # Display blank or invalid form
    context = {
        "form": form,
    }
    return render(request, "hobby/create_topic.html", context)


@login_required
def create_entry(request, topic_id=0):
    # topic_id is used to set the initial state of the topic combo box

    print(f'in create_entry()')
    print(f'{request.method=}')

    # Restrict the topic list to the users topics
    queryset = Topic.objects.filter(owner=request.user)

    if request.method == 'POST':
        print(f'processing post request')
        form = EntryForm(request.POST)
        form.fields['topic'].queryset = queryset

        if form.is_valid():
            form.save()
            # print(vars(form.cleaned_data['topic']))
            my_id = form.cleaned_data['topic'].id
            return redirect('hobby:view_topic', my_id)
        else:
            print('form not valid')
    else:
        # No form data submitted, so create the form
        form = EntryForm(initial={'topic': topic_id})
        form.fields['topic'].queryset = queryset

    # Display blank or invalid form
    context = {
        "form": form,
    }
    return render(request, "hobby/create_entry.html", context)

@login_required
def edit_entry(request, entry_id):

    print(f'in edit_entry()')
    print(f'{request.method=}')

    # entry = Entry.objects.get(id=entry_id)
    entry = get_object_or_404(Entry, id=entry_id)

    if entry.topic.owner != request.user:
        raise Http404

    # Restrict the topic list to the users topics
    queryset = Topic.objects.filter(owner=request.user)

    if request.method == 'POST':
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            my_id = form.cleaned_data['topic'].id
            return redirect('hobby:view_topic', my_id)
        else:
            print('form not valid')
    else:
        # No form data submitted, so create the form
        form = EntryForm(instance=entry)
        form.fields['topic'].queryset = queryset

    # Display blank or invalid form
    context = {
        "form": form,
        "entry": entry
    }
    return render(request, "hobby/edit_entry.html", context)
