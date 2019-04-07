import csv
import xlwt
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import cloudinter.models as cm
import cloudinter.forms as cf

# Create your views here.
def index(request):
    return render(request, 'cloudinter/home.html')

def student_list(request):
    """
    this displays all student who applied on the site
    """
    query = cm.Student.objects.all()
    context = {'details': query}
    return render(request, 'cloudinter/student_list.html', context)

def student_interview(request):
    details = cm.Question.objects.all().order_by('-created_date')
    context = {'details' : details}
    return render(request, 'cloudinter/student_list.html', context)

def student_approve(request):
    detail = cm.Question.objects.filter(approved_student = True).order_by('-created_date')
    context = {'detail' : detail}
    return render(request, 'cloudinter/student_approved.html', context)

#function to display the full details of a student
def student_detail(request, pk):
    info = get_object_or_404(cm.Question, pk=pk)
    # infos = Comment.objects.filter(post=info).order_by('-created_date')
    return render(request, 'cloudinter/student_detail.html', {'info' : info})


def new_interview(request):
    if request.method == "POST":
        form = cf.QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            #uncommenting the line below would make post published instantly
            post.published_date = timezone.now()
            post.save()
            return redirect('student_list')
    else:
        form = cf.QuestionForm()
    return render(request, 'cloudinter/new_interview.html', {'form': form})

#Function to add comment to a student question
def add_comment_to_student(request, pk):
    post = get_object_or_404(cm.Question, pk=pk)
    if request.method == "POST":
        form = cf.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('student_detail', pk=post.pk)
    else:
        form = cf.CommentForm()
    return render(request, 'cloudinter/add_comment_to_student.html', {'form': form})


def inview(request):
    detail = cm.Question.objects.filter(approved_student = False).order_by('-created_date')
    # detail = Question.objects.all()
    context = {'detail' : detail}
    return render(request, 'cloudinter/student_inview.html', context)


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="details.csv"'

    writer = csv.writer(response)
    writer.writerow(['Full Name', 'Address', 'Interviewed date'])

    users = cm.Question.objects.all().order_by('-created_date').values_list('fullname', 'address', 'created_date')
    for user in users:
        writer.writerow(user)

    return response



def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Question')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Full Name', 'Address', 'Interviewed date', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    # rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    rows = cm.Question.objects.filter(approved_student = True).order_by('-created_date').values_list('fullname', 'address', 'created_date')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response