from django.contrib import admin
from pages.models import Post, Comment, Student, Course, Enrollment
# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "body")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    inlines = [CommentInLine]               # Attach the inline

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_at")
    search_fields = ("author", "test")
    list_filter = ("created_at",)

# @admin.register(Student)

# @admin.register(Course)

# @admin.register(Enrollment)


#admin.site.register(Enrollment)