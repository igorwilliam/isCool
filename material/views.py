from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required

from discipline.models import Discipline, RegisterStudent
from .models import Material
from .forms import MaterialForm

# Create your views here.

@login_required
def addMaterial(request):

    if request.user.is_teacher == False:
        return redirect('error')

    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            sucess = True
        else:
            print(form.errors)

    else:
        form = MaterialForm()

    context = {
        'form': MaterialForm,
        'disciplines': Discipline.objects.all(),
    }

    return render(request, 'material/add-material.html', context)

def listMaterial(request):

    context = {
        'materials': Material.objects.all(),
        'registers': RegisterStudent.objects.all(),
    }

    return render(request, 'material/list-material.html', context)

def editMaterial(request, id):

    if request.user.is_teacher == False:
        return redirect('error')

    material = get_object_or_404(Material, id=id)
    if request.method == 'POST':
        form = MaterialForm(data=(request.POST, request.FILE), instance=material)
        if form.is_valid():
            form.save()
            return redirect('material:listMaterial')
    else:
        form = MaterialForm(instance=material)

    context = {
        'form': form,
        'edit': 'edit',
        'material': material,
    }

    return render(request,'material/add-material.html', context)
