from django.db import models
from django.utils import timezone

class project(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=35)
    address = models.CharField(max_length=140)
    image = models.ImageField(upload_to='project')





def __str__ (self):
    return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def copy(self):
        copied_post = BlogPost.objects.create(
            title=self.title,
            body=self.body,
            author=self.author,
            date_created=timezone.now()
        )

        for comment in self.comments.all():
            Comment.objects.create(
                blog_post=copied_post,
                text=comment.text
            )

        # Return the ID of the new post
        return copied_post.id

class Comment (models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
