from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

# This tweet_list function will list all tweets and allow users to create new tweets.
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            tweet_create = form.save(commit=False)
            tweet_create.user = request.user
            tweet_create.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

# This tweet_edit function will allow users to edit their tweets.
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id)
    if request.method == 'POST':
        form = TweetForm(
            request.POST,
            request.FILES,
            instance=tweet # isinstance is used for edit propose.
        )
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance = tweet)
    return render(request, 'tweet_form.html', {'form': form})
    
# This tweet_delete function will allow users to delete their tweets.
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(
        Tweet,
        pk = tweet_id,
        user = request.user
    )
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})