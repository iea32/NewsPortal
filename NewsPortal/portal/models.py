from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()

    def __str__(self):
        return f'{self.user}'

    def update_rating(self):
        post_author = Post.objects.filter(author = self.id, Post_type = self.author)
        total_post_rating = 0
        for post in post_author:
            total_post_rating += post.Post_rating * 3

        total_author_comment_rating = 0
        for comments in Comment.objects.filter(user = self.author):
            total_author_comment_rating += comments.comment_rating

        total_author_post_rating = 0
        for comments in Comment.objects.filter(post = post_author):
            total_author_post_rating += comments.comment_rating

        self.author_rating = total_post_rating + total_author_comment_rating + total_author_post_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return f'{self.name.title()}'


class Post(models.Model):
    article = 'a'
    news = 'n'

    POST_TYPE = [
        (article, "Статья"),
        (news, "Новость")
    ]

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    post_type = models.CharField(max_length = 1, choices = POST_TYPE, default = article)
    created = models.DateTimeField(auto_now_add = True)
    cats = models.ManyToManyField(Category, through = 'PostCategory')
    title = models.CharField(max_length = 255)
    text = models.TextField()
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]} ...'



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()