from django.http import HttpResponse 

from django.template import loader
#from AppCoder.models 

def home (self,name):
    return HttpResponse(f'Hola soy {name}')

def homePage (self):
    lista = [1,2,3,4,5,6,7,8,9]
    data = {'nombre':'Edgar', 'apellido':'Diaz', 'lista':lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

#def cursos (self):
    #planilla = loader.get_template('cursos.html')

    #documento = planilla.render()
    return HttpResponse(documento)