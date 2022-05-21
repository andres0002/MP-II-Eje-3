from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import DatosUsuario
from users.forms import UserForm

# Create your views here.

class ListUsers(View):
    template_name = 'list_user.html'

    def get_queryset(self):
        return DatosUsuario.objects.all()

    def get_context_data(self, **kwargs):
        context =  {}
        context['users'] = self.get_queryset()
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

class AddUser(View):
    template_name = 'add_user.html'
    form_class = UserForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El usuario se adicionó correctamente')

        else:
            messages.add_message(request, messages.ERROR, 'El usuario no se pudo adicionar')
        return redirect('list_user')

class VisualizeUser(View):
    template_name = 'visualize_user.html'
    form_class = UserForm

    def get(self, request, cedula):
        user = DatosUsuario.objects.get(cedula=cedula)
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})

class UpdateUser(View):
    template_name = 'update_user.html'
    form_class = UserForm

    def get(self, request, cedula):
        user = DatosUsuario.objects.get(cedula=cedula)
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, cedula):
        user = DatosUsuario.objects.get(cedula=cedula)
        form = self.form_class(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El usuario se modificó correctamente')
        else:
            messages.add_message(request, messages.ERROR, 'El usuario no se pudo modificar')
        return redirect('list_user')

class DeleteUser(View):
    template_name = 'delete_user.html'
    form_class = UserForm

    def get(self, request, cedula):
        user = DatosUsuario.objects.get(cedula=cedula)
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, cedula):
        user = DatosUsuario.objects.get(cedula=cedula)
        user.delete()
        messages.add_message(request, messages.INFO, "El usuario se borró correctamente")
        return redirect('list_user')