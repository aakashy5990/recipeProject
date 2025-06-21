from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Recipe
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum
# Create your views here.

@login_required(login_url="/login/")
def home(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")

        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        Recipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,
        )
        return redirect('home')
    else:
        queryset = Recipe.objects.all()
        heading = "Recipe Project Using Django"
        context = {'heading':heading}
        # context = {'receipes':queryset}
        return render(request,'vege/recipe.html',context)



#delete logic
def delete(request, id):
    if request.method == "POST":
        pi = Recipe.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/showdata/')
    

#update logic
def edit(request,id):
    queryset = Recipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_images')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/showdata/')

    context = {'receipe':queryset}
    return render(request,'vege/updatereceipe.html',context)

#datashow login
def showdata(request):
    queryset = Recipe.objects.all()
    context = {'receipes':queryset}


    #search logic
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        # print(request.GET.get('search'))
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
        context = {'receipes':queryset}
        return render(request,'vege/showdata.html',context)


    return render(request,'vege/showdata.html',context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')

    return render(request,'vege/login.html')

def logout_page(request):
    logout(request)
    return redirect('home')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.warning(request,"Username can't exist")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()
        messages.success(request,"Account created successfully!!!")
        return redirect('/register/')
    return render(request,'vege/register.html')



def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        # queryset = queryset.filter(student_name__icontains = search )
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains= search) |
            Q(student_age__icontains= search)
            )

    paginator = Paginator(queryset,10)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    print(page_obj.object_list)
    return render(request, 'vege/student.html' ,{'queryset':page_obj})


def see_marks(request,student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    print(queryset)
    student_names = queryset.values_list('student__student_name', flat=True).first()
    student_id = queryset.values_list('student__student_id__student_id', flat=True).first()
    # student_names = queryset.first().student.student_name
    print(student_names)
    print(student_id)

    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    print(total_marks)
    return render(request,'vege/see_marks.html',{
        'queryset':queryset,
        'total_marks' : total_marks,
        'student_names':student_names,
        'student_id':student_id,
        })