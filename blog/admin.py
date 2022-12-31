from django.contrib import admin
from marketing.models import Signup
from posts.models import PostView, Author, Category, Comment, Post

admin.site.register(Signup)
admin.site.register(Author)
admin.site.register(PostView)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
