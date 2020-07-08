"""
Views for accessing and changing the Menu models
"""
from django.urls import reverse, reverse_lazy
from django.forms.models import inlineformset_factory
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Menu, MenuCategory


class MenuList(ListView):
    """Shows a list of all the menus available"""

    model = Menu
    paginate_by = 15
    template_name = "menu/list.html"


class MenuDetail(DetailView):
    """Shows a full Menu as if a customer was reading it"""

    model = Menu
    template_name = "menu/detail.html"


class MenuCreate(CreateView):
    """Allows creation of Menu models"""

    model = Menu
    template_name = "menu/create.html"
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('menu:detail', kwargs={'pk': self.object.uuid})


class MenuDelete(DeleteView):
    """Allows deletion of Menu models"""

    model = Menu
    template_name = "menu/delete.html"
    success_url = reverse_lazy('menu:list')


class MenuUpdate(UpdateView):
    """Allows updating of Menu models"""

    model = Menu
    template_name = "menu/update.html"
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('menu:detail', kwargs={'pk': self.object.uuid})


class MenuCategoryCreate(CreateView):
    """Allows creation of categories"""

    model = MenuCategory
    template_name = "menu/create-category.html"
    fields = ['title', 'description']

    def get_parent_menu(self):
        return Menu.objects.get(uuid=self.kwargs['menu_pk'])

    def get_queryset(self):
        return super().get_queryset().filter(menu=self.get_parent_menu())

    def get_success_url(self):
        return reverse('menu:detail', kwargs={'pk': self.get_parent_menu().uuid}) + f'#{self.object.title}'

    def form_valid(self, form):
        form.instance.menu = self.get_parent_menu()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.get_parent_menu()
        return context


class MenuCategoryDelete(DeleteView):
    """Allows deletion of categories"""

    model = MenuCategory

    def get_parent_menu(self):
        return Menu.objects.get(uuid=self.kwargs['menu_pk'])

    def get_success_url(self):
        return reverse('menu:detail', kwargs={'pk': self.get_parent_menu().uuid}) + f'#{self.object.title}'

    def get_queryset(self):
        return super().get_queryset().filter(menu=self.get_parent_menu())

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class MenuCategoryUpdate(UpdateView):
    """Allows updating of categories"""

    model = MenuCategory
    template_name = "menu/update-category.html"
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('menu:detail', kwargs={'pk': self.object.uuid})

    def get_parent_menu(self):
        return Menu.objects.get(uuid=self.kwargs['menu_pk'])

    def get_success_url(self):
        return reverse('menu:detail', kwargs={'pk': self.get_parent_menu().uuid}) + f'#{self.object.title}'

    def get_queryset(self):
        return super().get_queryset().filter(menu=self.get_parent_menu())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.get_parent_menu()
        return context
