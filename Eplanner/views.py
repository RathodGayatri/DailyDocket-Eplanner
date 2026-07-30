from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from app.models import ExamSetting, SignUp,Expenditure,Todo
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from app.forms import Todo
from django.views.decorators.http import require_http_methods
import json
from datetime import datetime
import random
import string

from django.utils import timezone



def generate_otp():
    return ''.join(random.choices(string.digits, k=6))
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

def MySignUp(request):
    if request.method == 'POST':
        # Get form data
        email = request.POST.get('email')
        
        # Check if user exists and is already verified
        try:
            existing_user = SignUp.objects.get(email=email)
            if existing_user.is_verified:
                messages.info(request, 'Email already verified. Please login.')
                return redirect('login')
            # If not verified, generate new OTP
            otp = existing_user.generate_otp()
        except SignUp.DoesNotExist:
            # Create new user
            user = SignUp(
                name=request.POST.get('name'),
                mobile=request.POST.get('mob'),
                email=email,
                pass1=request.POST.get('pass')
            )
            otp = user.generate_otp()
        
        # Send OTP email
        send_mail(
            'Your Verification Code',
            f'Your OTP is: {otp}\nValid for 2 minutes',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        
        request.session['verify_email'] = email
        return redirect('verify_otp')
    
    return render(request, 'newreg.html')

def verify_otp(request):
    # Check if email exists in session
    email = request.session.get('verify_email')
    if not email:
        messages.error(request, 'Session expired. Please sign up again.')
        return redirect('signup')

    try:
        user = SignUp.objects.get(email=email)
    except SignUp.DoesNotExist:
        messages.error(request, 'User not found. Please sign up again.')
        return redirect('signup')

    # Calculate remaining time
    remaining_time = 0
    if user.otp_created_at:
        elapsed = (timezone.now() - user.otp_created_at).total_seconds()
        remaining_time = max(0, 120 - int(elapsed))  # 2 minutes in seconds

    if request.method == 'POST':
        if user.is_verified:
            messages.info(request, 'Account already verified. Please login.')
            return redirect('login')

        if remaining_time <= 0:
            messages.error(request, 'OTP expired. Please request a new one.')
            return redirect('verify_otp')

        entered_otp = request.POST.get('otp', '').strip()
        if not entered_otp.isdigit() or len(entered_otp) != 6:
            messages.error(request, 'Invalid OTP format. Please enter a 6-digit number.')
            return render(request, 'verify_otp.html', {
                'email': email,
                'remaining_time': remaining_time
            })

        if user.otp == entered_otp:
            try:
                # Update user verification status
                user.is_verified = True
                user.verified_at = timezone.now()
                user.save()
                
                # Prepare welcome email
                login_url = request.build_absolute_uri(reverse('login'))
                email_subject = 'Welcome to Engineer\'s Daily Planner!'
                email_body = f"""Hello {user.name},

                
Thank you for signing up with Engineer's Daily Planner!
Your account has been successfully verified.

Start organizing your engineering tasks and boost your productivity today!

# Login to your account: {login_url}

If you have any questions, please contact our support team.

Best regards,
Engineer's Daily Planner Team
"""
                # Send welcome email
                send_mail(
                    email_subject,
                    email_body,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                
                # Clean up session
                if 'verify_email' in request.session:
                    del request.session['verify_email']
                
                messages.success(request, 'Verification successful! Please login.')
                return redirect('login')
                
            except Exception as e:
                # Log the error for debugging
                print(f"Error during verification: {str(e)}")
                messages.error(request, 'An error occurred during verification. Please try again.')
                return redirect('verify_otp')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return render(request, 'verify_otp.html', {
                'email': email,
                'remaining_time': remaining_time
            })

    return render(request, 'verify_otp.html', {
        'email': email,
        'remaining_time': remaining_time
    })
def resend_otp(request):
    email = request.session.get('verify_email')
    if email:
        try:
            user = SignUp.objects.get(email=email)
            new_otp = generate_otp()  # Your OTP generation function
            user.otp = new_otp
            user.save()
            
            # Send email with new OTP
            send_mail(
                'Your New Verification OTP',
                f'Your new OTP is: {new_otp} (valid for 2 minutes)',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'New OTP sent successfully!')
        except SignUp.DoesNotExist:
            messages.error(request, 'Error resending OTP. Please try again.')
    
    return redirect('verify_otp')

def MyLogin(request):
    if request.method == 'POST':
        em = request.POST['email']
        pass1 = request.POST['pass']
        
        try:
            user = SignUp.objects.get(email=em, pass1=pass1)
            if user.is_verified:
                if em == 'admin@gmail.com':
                    return HttpResponseRedirect('/admin')
                else:
                    return HttpResponseRedirect('/userdash')
            else:
                messages.error(request, 'Account not verified. Please check your email for OTP.')
        except SignUp.DoesNotExist:
            messages.error(request, 'Invalid email or password')
        
        return HttpResponseRedirect('/login')
    
    return render(request, 'newlogin.html')

def MyAdmin(request):
	return render(request,'userdash.html')

def notice_view(request):
    return render(request, 'notice.html')

def about_view(request):
    return render(request, 'about.html')

def exam_tracker_view(request):
    return render(request, 'exam1.html')

def expenditure_view(request):
    return render(request, 'expenditure.html')

def notemyday_view(request):
    return render(request, 'index3.html')

def logout_view(request):
    return render(request, 'logout.html')

def project_tracker_view(request):
    return render(request, 'projectracker.html')

def quiz_view(request):
    return render(request, 'qu.html')

# def todo_list_view(request):
#     return render(request, 'todo1.html')

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.models import Expenditure

class ExpenditureListCreate(APIView):
    def get(self, request):
        expenses = Expenditure.objects.filter(user=request.user)
        data = [{
            'id': exp.id,
            'day': exp.day,
            'amount': str(exp.amount),
            'category': exp.category,
            'date_added': exp.date_added
        } for exp in expenses]
        return Response(data)

    def post(self, request):
        try:
            expense = Expenditure.objects.create(
                user=request.user,
                day=request.data.get('day'),
                amount=request.data.get('amount'),
                category=request.data.get('category')
            )
            return Response({
                'status': 'success',
                'id': expense.id
            }, status=201)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=400)

class ExpenditureDetail(APIView):
    def delete(self, request, pk):
        try:
            expense = Expenditure.objects.get(id=pk, user=request.user)
            expense.delete()
            return Response({'status': 'success'})
        except Expenditure.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Expense not found'
            }, status=404)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=400)

# from django.shortcuts import render,redirect, get_object_or_404
# from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from app.models import SignUp, Note
from django.utils import timezone  
import json
@login_required
def notemyday_view(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'index3.html', {'notes': notes})

#from django.utils import timezone  # Make sure this import exists at the top

@csrf_exempt
@login_required
def add_note(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            note = Note.objects.create(
                user=request.user,
                title=data.get('title', ''),
                content=data.get('content', ''),
                created_at=timezone.now()  # This already uses timezone-aware datetime
            )
            return JsonResponse({
                'success': True,
                'note': {
                    'id': note.id,
                    'title': note.title,
                    'content': note.content,
                    'created_at': note.created_at.astimezone(timezone.get_current_timezone()).strftime("%b %d, %Y %I:%M %p")
                    # ^^^ Changed this line to use timezone conversion ^^^
                }
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
    return JsonResponse({
        'success': False,
        'error': 'Invalid request method'
    }, status=405)

@csrf_exempt  # Only if you're having CSRF issues, otherwise remove this
def delete_note(request, note_id):
    if request.method == 'POST':
        try:
            note = Note.objects.get(id=note_id, user=request.user)
            note.delete()
            return JsonResponse({'success': True})
        except Note.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Note not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)
    


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from app.models import Todo
import json

@login_required
def todo_list_view(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todo1.html', {'todos': todos})

# views.py
@csrf_exempt
@login_required
def add_todo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            todo = Todo.objects.create(
                user=request.user,
                title=data.get('title'),
                completed=False,
                priority=data.get('priority', 'M')
            )
            return JsonResponse({
                'success': True,
                'todo': {
                    'id': todo.id,
                    'title': todo.title,
                    'completed': todo.completed,
                    'priority': todo.priority,  # Return raw value
                    'created_at': todo.created_at.astimezone(timezone.get_current_timezone()).strftime("%b %d, %Y %I:%M %p")
                }
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
    return JsonResponse({
        'success': False,
        'error': 'Invalid request method'
    }, status=405)

@csrf_exempt
@login_required
def edit_todo(request, todo_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            todo = Todo.objects.get(id=todo_id, user=request.user)
            todo.title = data.get('title', todo.title)
            todo.priority = data.get('priority', todo.priority)
            todo.save()
            return JsonResponse({
                'success': True,
                'todo': {
                    'id': todo.id,
                    'title': todo.title,
                    'completed': todo.completed,
                    'priority': todo.priority,
                    'created_at': todo.created_at.astimezone(timezone.get_current_timezone()).strftime("%b %d, %Y %I:%M %p")
                }
            })
        except Todo.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Todo not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

@csrf_exempt
@login_required
def toggle_todo(request, todo_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            todo = Todo.objects.get(id=todo_id, user=request.user)
            todo.completed = data.get('completed', False)
            todo.save()
            return JsonResponse({'success': True})
        except Todo.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Todo not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

@csrf_exempt
@login_required
def delete_todo(request, todo_id):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(id=todo_id, user=request.user)
            todo.delete()
            return JsonResponse({'success': True})
        except Todo.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Todo not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
# views.py
@login_required
def get_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id, user=request.user)
        return JsonResponse({
            'id': todo.id,
            'title': todo.title,
            'priority': todo.priority,
            'completed': todo.completed,
            'created_at': todo.created_at.astimezone(timezone.get_current_timezone()).strftime("%b %d, %Y %I:%M %p")
        })
    except Todo.DoesNotExist:
        return JsonResponse({'error': 'Todo not found'}, status=404)




from django.http import JsonResponse

def get_quiz_questions(request):
    # Example implementation - replace with your actual quiz questions
    questions = [
        {
            'question': 'Sample question 1',
            'options': ['Option 1', 'Option 2', 'Option 3'],
            'answer': 'Option 1'
        },
        # Add more questions as needed
    ]
    return JsonResponse({'questions': questions})
