from django.contrib import admin
from .models import Post, Profile, Relationship

# Registro de los diferentes modelos.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)