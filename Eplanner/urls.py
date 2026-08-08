```python
from django.contrib import admin
from django.urls import path, include
from Eplanner import views
from django.shortcuts import redirect

app_name = 'app'

urlpatterns = [
    # Homepage → Login page
    path('', lambda request: redirect('login')),

    path('admin/', admin.site.urls),

    # Django authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),

    # Authentication
    path('login/', views.MyLogin, name='login'),
    path('signup/', views.MySignUp, name='signup'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('resend-otp/', views.resend_otp, name='resend_otp'),

    # Dashboard & General Pages
    path('userdash/', views.MyAdmin, name='userdash'),
    path('notice/', views.notice_view, name='notice'),
    path('about/', views.about_view, name='about'),

    # Exam Tracker
    path('exam-tracker/', views.exam_tracker_view, name='exam_tracker'),

    # Expenditure
    path('expenditure/', views.expenditure_view, name='expenditure'),

    # Note My Day
    path('notemyday/', views.notemyday_view, name='notemyday'),

    # Logout
    path('logout/', views.logout_view, name='logout'),

    # Project Tracker
    path('project-tracker/', views.project_tracker_view, name='project_tracker'),

    # Quiz
    path('quiz/', views.quiz_view, name='quiz'),

    # To-Do List
    path('todo/', views.todo_list_view, name='todo_list'),
    path('add-todo/', views.add_todo, name='add_todo'),
    path('toggle-todo/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
    path('delete-todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('edit-todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('get-todo/<int:todo_id>/', views.get_todo, name='get_todo'),

    # Expenditure REST API
    path(
        'api/expenses/',
        views.ExpenditureListCreate.as_view(),
        name='expense-list'
    ),
    path(
        'api/expenses/<int:pk>/',
        views.ExpenditureDetail.as_view(),
        name='expense-detail'
    ),

    # Notes
    path('add-note/', views.add_note, name='add_note'),
    path(
        'delete-note/<int:note_id>/',
        views.delete_note,
        name='delete_note'
    ),
]
```