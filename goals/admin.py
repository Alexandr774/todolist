from django.contrib import admin
from goals.models import GoalCategory, Goal, GoalComment


@admin.register(GoalCategory)
class GoalCatAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "updated")
    search_fields = ("title", "user")


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user",)
    search_fields = ("title", "user")


@admin.register(GoalComment)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "text")
    search_fields = ("title", "user")