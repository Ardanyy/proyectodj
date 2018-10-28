from django.shortcuts import render,get_object_or_404,get_object_or_404,HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy   
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required 
from django.utils.decorators import method_decorator    
from app.models import Juego,Plataformas,Controles,Genero,Distribuidora,Slider
from django.contrib.auth.decorators import login_required

class Usuarioslogin(object):
    """
    usuario logeado
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Usuarioslogin,self).dispatch(request,*args,**kwargs)

class HomePageView(TemplateView):

    template_name = "app/inicio.html"
    def get (self, request, *args, **kwargs):
        return render(request, self.template_name,{'title':"Bienvenido"})

class Detailjuego(DetailView):
    model = Juego
    
@method_decorator(staff_member_required, name='dispatch')
class PageListjuego(ListView):
    model = Juego
@method_decorator(staff_member_required, name='dispatch')
class PageListplataformas(ListView):
    model = Plataformas

@method_decorator(staff_member_required, name='dispatch')
class PageListControles(ListView):
    model = Controles
@method_decorator(staff_member_required, name='dispatch')
class PageListGeneros(ListView):
    model = Genero
@method_decorator(staff_member_required, name='dispatch')
class PageListDistribuidora(ListView):
    model = Distribuidora

@method_decorator(staff_member_required, name='dispatch')
class PageListSlider(ListView):
    model = Slider

@method_decorator(staff_member_required, name='dispatch')
class Createjuego(CreateView):
    model = Juego
    fields = ['nombre','creadores','Foto','Descripcion','distribuidora','genero','plataformas','Descripcion']
    success_url = reverse_lazy('app:inicio')

@method_decorator(staff_member_required, name='dispatch')
class Createplataformas(CreateView):
    model = Plataformas
    fields = ['nombre','Foto','jubailidad','descripcion']
    success_url = reverse_lazy('app:plataformas')

@method_decorator(staff_member_required, name='dispatch')
class CreateControles(CreateView):
    model = Controles
    fields = ['nombre','descripcion']
    success_url = reverse_lazy('app:controles') 

@method_decorator(staff_member_required, name='dispatch')
class CreateGenero(CreateView):
    model = Genero
    fields = ['nombre','descripcion']
    success_url = reverse_lazy('app:generos')   

@method_decorator(staff_member_required, name='dispatch')
class CreateDistribuidora(CreateView):
    model = Distribuidora
    fields = ['nombred','industria','fundacion','sede','Foto']
    success_url = reverse_lazy('app:distribuidora')

@method_decorator(staff_member_required, name='dispatch')
class CreateSlider(CreateView):
    model = Slider
    fields = ['nombre','Foto','descripcion']
    success_url = reverse_lazy('app:slider')

@method_decorator(staff_member_required, name='dispatch')
class Updatejuego(UpdateView):
    model = Juego
    fields = ['nombre','creadores','Foto','Descripcion','distribuidora','genero','plataformas','Descripcion']
    success_url = reverse_lazy('app:inicio')

@method_decorator(staff_member_required, name='dispatch')
class Updateplataformas(UpdateView):
    model = Plataformas
    fields = ['nombre','Foto','jubailidad','descripcion']
    success_url = reverse_lazy('app:plataformas')

@method_decorator(staff_member_required, name='dispatch')
class Updatecontroles(UpdateView):
    model = Controles
    fields = ['nombre','descripcion']
    success_url = reverse_lazy('app:controles')

@method_decorator(staff_member_required, name='dispatch')
class UpdateGenero(UpdateView):
    model = Genero
    fields = ['nombre','descripcion']
    success_url = reverse_lazy('app:generos')  

@method_decorator(staff_member_required, name='dispatch')
class UpdateDistribuidora(UpdateView):
    model = Distribuidora
    fields = ['nombred','industria','fundacion','sede','Foto']
    success_url = reverse_lazy('app:distribuidora')

@method_decorator(staff_member_required, name='dispatch')
class UpdateSlider(UpdateView):
    model = Slider
    fields = ['nombre','Foto','descripcion']
    success_url = reverse_lazy('app:slider')
    
@method_decorator(staff_member_required, name='dispatch')
class Deletejuego(DeleteView):
    model = Juego
    success_url = reverse_lazy('app:inicio')

@method_decorator(staff_member_required, name='dispatch')
class DeletePlataformas(DeleteView):
    model = Plataformas
    success_url = reverse_lazy('app:plataformas')

@method_decorator(staff_member_required, name='dispatch')
class DeleteControl(DeleteView):
    model = Controles
    success_url = reverse_lazy('app:controles')

@method_decorator(staff_member_required, name='dispatch')
class DeleteGenero(DeleteView):
    model = Genero
    success_url = reverse_lazy('app:generos')

@method_decorator(staff_member_required, name='dispatch')
class DeleteDistribuidora(DeleteView):
    model = Distribuidora
    success_url = reverse_lazy('app:generos')
    
@method_decorator(staff_member_required, name='dispatch')
class DeleteSlider(DeleteView):
    model = Slider
    success_url = reverse_lazy('app:slider')