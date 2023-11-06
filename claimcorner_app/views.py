from django.shortcuts import render
from .models import Post, Comment

def index(request):
    # Logic to fetch recent blog posts
    recent_posts = Post.objects.order_by('-created_at')[:4]
    return render(request, 'claimcorner_app/index.html', {'recent_posts': recent_posts})

def blog(request):
    # Logic to fetch all blog posts
    all_posts = Post.objects.all()
    return render(request, 'claimcorner_app/blog.html', {'all_posts': all_posts})

def news(request):
    # Logic to fetch and display news articles
    # Implement logic here to retrieve news articles
    return render(request, 'claimcorner_app/news.html')

def privacy_policy(request):
    return render(request, 'claimcorner_app/privacy_policy.html')


