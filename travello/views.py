from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination, Comment
from .forms import CommentForm, ReplyForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests, 'is_authenticated': request.user.is_authenticated})


def details(request, id):
    destination = get_object_or_404(Destination, pk=id)
    comments = destination.comments.filter(parent__isnull=True)  # Only top-level comments
    comment_form = CommentForm()
    reply_form = ReplyForm()

    if request.method == "POST":
        if 'comment_form' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.destination = destination
                comment.user = request.user
                comment.save()
                return redirect('details', id=id)
        elif 'reply_form' in request.POST:
            form = ReplyForm(request.POST)
            parent_id = request.POST.get('parent_id')
            if form.is_valid():
                reply = form.save(commit=False)
                reply.destination = destination
                reply.user = request.user
                if parent_id:
                    parent_comment = Comment.objects.get(id=parent_id)
                    reply.parent = parent_comment
                reply.save()
                return redirect('details', id=id)

    return render(request, 'details.html', {
        'destination': destination,
        'comments': comments,
        'comment_form': comment_form,
        'reply_form': reply_form
    })

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
        comment.dislikes.remove(request.user)  # Ensure user can't like and dislike at the same time
    return redirect('details', id=comment.destination.id)

@login_required
def dislike_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.dislikes.all():
        comment.dislikes.remove(request.user)
    else:
        comment.dislikes.add(request.user)
        comment.likes.remove(request.user)  # Ensure user can't like and dislike at the same time
    return redirect('details', id=comment.destination.id)
