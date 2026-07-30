# from django.contrib import admin
# from app.models import MySignUp

# from .models import LoginHistory
# # Register your models here.
# admin.site.register(MySignUp)
# # admin.site.register(Studentreg)
# # admin.site.register(AdminNotice)
# # admin.site.register(Notification)
# admin.site.register(LoginHistory)

# #admin.site.register(Menubar)


from django.contrib import admin
from app.models import SignUp,Expenditure,Note
# Register your models here.

admin.site.register(SignUp)
admin.site.register(Note)

@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'amount', 'category')
    list_filter = ('day', 'category')
    search_fields = ('user__username', 'category')

# from .models import TimeLog
# admin.site.register(TimeLog)

# Choose ONE of these registration methods, not both:

# Option 1: Using decorator (recommended)
# @admin.register(Note)
# class NoteAdmin(admin.ModelAdmin):
#     list_display = ('user', 'title', 'created_at')
#     list_filter = ('user', 'created_at')
#     search_fields = ('title', 'text', 'user__username')
#     readonly_fields = ('created_at',)
# OR Option 2: Using admin.site.register()
'''
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('title', 'text', 'user__username')
    readonly_fields = ('created_at',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(Note, NoteAdmin)
'''
from app.models import TimeLog

@admin.register(TimeLog)
class TimeLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'task_name', 'date', 'duration_formatted', 'created_at')
    list_filter = ('user', 'task_name', 'date')
    search_fields = ('user__username', 'task_name')

# from django.contrib import admin
# from .models import Note

# @admin.register(Note)
# class NoteAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user', 'created_at')
#     search_fields = ('title', 'content', 'user__username')
from app.models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'get_priority_display', 'completed', 'created_at')
    list_filter = ('completed', 'priority', 'created_at')
    search_fields = ('user__username', 'title')

#quiz   
# from .models import QuizQuestion, QuizChoice, UserQuizAttempt, UserAnswer

# class QuizChoiceInline(admin.TabularInline):
#     model = QuizChoice
#     extra = 1

# @admin.register(QuizQuestion)
# class QuizQuestionAdmin(admin.ModelAdmin):
#     inlines = [QuizChoiceInline]
#     list_display = ('question_text', 'category', 'question_type')
#     search_fields = ('question_text', 'category')
#     list_filter = ('category', 'question_type')

# # @admin.register(UserQuizAttempt)
# # class UserQuizAttemptAdmin(admin.ModelAdmin):
# #     list_display = ('user', 'score', 'total_questions', 'started_at', 'completed_at', 'duration_formatted')
# #     list_filter = ('completed_at', 'user')
# #     readonly_fields = ('started_at', 'completed_at', 'duration_formatted')
    
# # OPTION 1: Using decorator (recommended)
# # Either use the decorator:
# @admin.register(UserQuizAttempt)
# class UserQuizAttemptAdmin(admin.ModelAdmin):
#     list_display = ["user", "quiz", "score"]

# # OR use the function call (but not both):
# admin.site.register(UserQuizAttempt, UserQuizAttemptAdmin)

# # OR OPTION 2: Using admin.site.register (but not both!)
# # admin.site.register(UserQuizAttempt, UserQuizAttemptAdmin)

# def duration_formatted(self, obj):
#         return obj.duration_formatted
# duration_formatted.short_description = 'Duration'
# @admin.register(UserAnswer)
# class UserAnswerAdmin(admin.ModelAdmin):
#     list_display = ('attempt', 'question', 'is_correct')
#     list_filter = ('is_correct', 'attempt__user')

# # #exam
# from django.contrib import admin
# from .models import UserQuizAttempt, Exam  # or whatever models you need

# # Either use the decorator approach (recommended):
# @admin.register(UserQuizAttempt)
# class UserQuizAttemptAdmin(admin.ModelAdmin):
#     pass
# @admin.register(Exam)
# class ExamAdmin(admin.ModelAdmin):
#     list_display = ('name', 'date', 'user')

# # OR the registration approach (but not both!):
# # admin.site.register(UserQuizAttempt, UserQuizAttemptAdmin)
# # admin.site.register(Exam, ExamAdmin)