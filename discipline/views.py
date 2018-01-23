from django.shortcuts import render, get_object_or_404, redirect

from discipline.models import Discipline, RegisterStudent

from discipline.forms import DisciplineForm, RegisterStudentForm

# Create your views here.
def addDiscipline(request):

    if request.user.is_teacher == False:
        return redirect('error')

    success = False
    if request.method == 'POST':
        form = DisciplineForm(request.POST)
        if form.is_valid:
            form.save()
            sucess = True
        else:
            print(form.errors)

    else:
        form = DisciplineForm()

    return render(request, 'discipline/add-discipline.html', {'form': form})

class ListDisciplineView(object):

    def __call__(self, request):


        if request.user.is_student == False:
            return redirect('error')

        if request.method == 'POST':
            form = RegisterStudentForm(request.POST)

            if form.is_valid:
                form.save()
            else:
                print(form.errors)
        else:
            form = RegisterStudentForm()

        context = {
            'form': RegisterStudentForm,
            'disciplines': Discipline.objects.all(),
            'registers': RegisterStudent.objects.get_queryset().filter(student=request.user),

        }

        return render(request, 'discipline/list-disciplines.html', context)

listDiscipline = ListDisciplineView()

class ManagerDisciplineView(object):

    def __call__(self, request):

        if request.user.is_teacher == False:
            return redirect('error')


        context = {
            'disciplines': Discipline.objects.all(),
            # 'disciplines': Discipline.objects.get_queryset().filter(id=request.user.id),
        }

        return render(request, 'discipline/manager-discipline.html', context)

managerDiscipline = ManagerDisciplineView()


class ListStudentView(object):

    def __call__(self, request):

        if request.user.is_teacher == False:
            return redirect('error')

        context = {
            'form': RegisterStudentForm,
            'registers': RegisterStudent.objects.all(),
        }

        return render(request, 'discipline/manager-student.html', context)

listStudent = ListStudentView()



class RegisterStudentView(object):

    def __call__(self, request, id):

        if request.user.is_teacher == False:
            return redirect('error')

        student = get_object_or_404(RegisterStudent, id=id)
        form = RegisterStudentForm(data=request.POST, instance=student)

        if form.is_valid():
            form.save();
            return redirect('discipline:listStudent')


registerStudent = RegisterStudentView()

class EditDisciplineView(object):

    def __call__(self, request, id):


        if request.user.is_teacher == False:
            return redirect('error')

        discipline = get_object_or_404(Discipline, id=id)
        if request.method == 'POST':
            form = DisciplineForm(data=request.POST, instance=discipline)
            if form.is_valid():
                form.save()
                return redirect('discipline:managerDiscipline')
        else:
            form = DisciplineForm(instance=discipline)

        context = {
            'form': form,
            'edit': 'edit',
        }

        return render(request,'discipline/add-discipline.html', context)

editDiscipline = EditDisciplineView()

def deleteDiscipline(request, id):

    if request.user.is_teacher == False:
        return redirect('error')

    discipline = Discipline.objects.get(id=id).delete()
    return redirect('discipline:managerDiscipline')
