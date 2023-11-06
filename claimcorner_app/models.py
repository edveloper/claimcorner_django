from django.db import models

class Category(models.Model):
    # Add your fields here
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'claimcorner_app'  # Add the app_label attribute

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=60)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    interested_categories = models.ManyToManyField(Category)

