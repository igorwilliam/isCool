from django.shortcuts import render

from discipline.models import Discipline

from discipline.forms import DisciplineForm

# Create your views here.
def addDiscipline(request):

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

        context = {
            'disciplines': Discipline.objects.all(),
        }

        return render(request, 'discipline/list-disciplines.html', context)

listDiscipline = ListDisciplineView() #criando view em forma de classes
