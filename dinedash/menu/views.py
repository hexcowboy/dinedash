from django.views.generic import DetailView, ListView

from .models import Menu, MenuItem, MenuCategory


class MenuList(ListView):
    """Shows a list of all the menus available"""
    model = Menu
    paginate_by = 15
    template_name = 'menu/list.html'


class MenuDetail(DetailView):
    """Shows a full Menu as if a customer was reading it"""
    model = Menu
    template_name = 'menu/detail.html'

    def get_context_data(self, **kwargs):
        """Fetch categories, items, and addons"""
        context = super().get_context_data(**kwargs)
        context['categories'] = MenuCategory.objects.filter(menu=self.get_object())
        return context
