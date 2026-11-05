from django.shortcuts import render,redirect
from .forms import TeacherForm
from .models import Teachers

def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Teachers.objects.create(
            name = cd['name'],
            email = cd['email'],
            phone_number = cd['phone_number'],
            bio = cd['bio'])
            #Logic to commit data to database
            return redirect('teachers_list')
    else:   
        form = TeacherForm()
    return render(request,'teachers/add_teacher.html',{'form':form})

def teachers_list(request):
    teachers = Teachers.objects.all()
    return render(request,'teachers/teachers_list.html',{'teachers':teachers})

def update_teachers(request,id):
    teacher = Teachers.objects.get(id=id)
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            teacher.name = cd['name'] 
            teacher.email = cd['email']
            teacher.phone_number = cd['phone_number']
            teacher.bio = cd['bio']
            teacher.save()
            return redirect('teachers_list')
    else:
        form = TeacherForm(initial={'name':teacher.name,
                                    'email':teacher.email,
                                    'phone_number':teacher.phone_number,
                                    'bio':teacher.bio})

    return render(request,'teachers/update_teacher.html',{'form':form})

def delete_teacher(request,id):
    teacher = Teachers.objects.get(id=id)
    teacher.delete()
    return redirect('teachers_list')
