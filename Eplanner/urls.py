

from django.contrib import admin
from django.urls import path,include
from Eplanner import views
from django.shortcuts import render

app_name='app'


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('login/', views.MyLogin, name='login'),
    path('signup/', views.MySignUp, name='signup'),  # Make sure this has name='signup'
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('resend-otp/', views.resend_otp, name='resend_otp'),
    path('userdash/', views.MyAdmin, name='userdash'),
    path('notice/', views.notice_view, name='notice'),
    path('about/', views.about_view, name='about'),
    
    path('exam-tracker/', views.exam_tracker_view, name='exam_tracker'),

    path('expenditure/', views.expenditure_view, name='expenditure'),
    path('notemyday/', views.notemyday_view, name='notemyday'),
    # path('add-note/', views.add_note, name='add_note'),
    # path('delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('logout/', views.logout_view, name='logout'),
    path('project-tracker/', views.project_tracker_view, name='project_tracker'),
    
    path('quiz/', views.quiz_view, name='quiz'),
    #path('api/get-quiz-questions/', views.get_quiz_questions, name='get_quiz_questions'),
    #path('api/submit-quiz-attempt/', views.submit_quiz_attempt, name='submit_quiz_attempt'),

    path('todo/', views.todo_list_view, name='todo_list'),
    path('add-todo/', views.add_todo, name='add_todo'),
    path('toggle-todo/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
    path('delete-todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('edit-todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('get-todo/<int:todo_id>/', views.get_todo, name='get_todo'),

    path('api/expenses/', views.ExpenditureListCreate.as_view(), name='expense-list'),
    path('api/expenses/<int:pk>/', views.ExpenditureDetail.as_view(), name='expense-detail'),
   
    path('add-note/', views.add_note, name='add_note'),
    path('delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
   
 ]

 
 
 

