from django.db import models
from django.contrib.auth.models import User
from datetime import date
import random
import string
from django.utils import timezone
class SignUp(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True)  # Changed to EmailField
    pass1 = models.CharField(max_length=20)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)

    def generate_otp(self):
        self.otp = ''.join(random.choices(string.digits, k=6))
        self.otp_created_at = timezone.now()
        self.save()
        return self.otp

    def is_otp_valid(self):
        if not self.otp_created_at:
            return False
        return (timezone.now() - self.otp_created_at).total_seconds() < 120  # 2 minutes
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
class Expenditure(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Shopping', 'Shopping'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]
    
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.day} - {self.category}: ₹{self.amount}"

def format_time(seconds):
    """Convert seconds to h m s format (reusable in models/templates)"""
    hrs = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hrs}h {mins}m {secs}s"

class TimeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)  # This should work with proper timezone settings
    duration_seconds = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)  # This will always be correct

    def __str__(self):
        return f"{self.user.username} - {self.task_name} ({self.duration_seconds}s)"

    @property
    def duration_formatted(self):
        return format_time(self.duration_seconds)


from django.contrib.auth import get_user_model

User = get_user_model()

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    remind_at = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    
    def __str__(self):
        return f"Reminder for {self.user.email} at {self.remind_at}"
    
# In models.py
# class Todo(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)  # Changed from 'task' to 'title'
#     # due_date = models.DateField(null=True, blank=True)  # Remove or keep if you need it
#     completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.title} - {'Completed' if self.completed else 'Active'}"
#todo
# models.py
class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    
    def __str__(self):
        return f"{self.title} - {'Completed' if self.completed else 'Active'}"
    

#quiz
# class QuizQuestion(models.Model):
#     QUESTION_TYPES = [
#         ('MC', 'Multiple Choice'),
#         ('TF', 'True/False'),
#     ]
    
#     category = models.CharField(max_length=100)
#     question_type = models.CharField(max_length=2, choices=QUESTION_TYPES, default='MC')
#     question_text = models.TextField()
#     correct_answer = models.CharField(max_length=200)
#     explanation = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.category}: {self.question_text[:50]}..."

# class QuizChoice(models.Model):
#     question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='choices')
#     choice_text = models.CharField(max_length=200)
#     is_correct = models.BooleanField(default=False)
    
#     def __str__(self):
#         return f"{self.question.question_text[:20]} - {self.choice_text[:20]}"

# from django.utils import timezone

# class UserQuizAttempt(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     score = models.IntegerField()
#     total_questions = models.IntegerField()
#     started_at = models.DateTimeField(auto_now_add=True)
#     completed_at = models.DateTimeField(null=True, blank=True)
#     duration_seconds = models.IntegerField(default=0)  # Store duration in seconds

#     def save(self, *args, **kwargs):
#         if self.completed_at and self.started_at:
#             self.duration_seconds = (self.completed_at - self.started_at).total_seconds()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.user.username} - {self.score}/{self.total_questions}"

#     @property
#     def duration_formatted(self):
#         return self.format_time(self.duration_seconds)

#     @staticmethod
#     def format_time(seconds):
#         hours = int(seconds // 3600)
#         minutes = int((seconds % 3600) // 60)
#         seconds = int(seconds % 60)
#         return f"{hours}h {minutes}m {seconds}s"

# class UserAnswer(models.Model):
#     attempt = models.ForeignKey(UserQuizAttempt, on_delete=models.CASCADE, related_name='user_answers')
#     question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
#     selected_answer = models.CharField(max_length=200)
#     is_correct = models.BooleanField()
    
#     def __str__(self):
#         return f"{self.attempt.user.username} - Q{self.question.id}"
    
# #exam
# from django.db import models
# from django.contrib.auth.models import User

# class Exam(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     date = models.DateTimeField()
#     description = models.TextField(blank=True)
    
#     def __str__(self):
#         return self.name

# class UserQuizAttempt(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
#     started_at = models.DateTimeField(auto_now_add=True)
#     finished_at = models.DateTimeField(null=True, blank=True)
#     score = models.IntegerField(null=True, blank=True)
    
#     def __str__(self):
#         return f"{self.user.username}'s attempt on {self.exam.name}"


from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
import random
import string
from django.utils import timezone

# ... (your existing models remain the same)

class ExamSubject(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.difficulty}) - {self.user.username}"

class ExamTimetable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    subject_name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=ExamSubject.DIFFICULTY_CHOICES)
    study_hours = models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.date} - {self.subject_name} ({self.study_hours} hrs)"

class ExamSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exam_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Exam settings for {self.user.username}"