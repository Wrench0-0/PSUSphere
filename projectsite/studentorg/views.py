from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from studentorg.models import Organization
from studentorg.forms import OrganizationForm


class HomePageView(ListView):
    model = Organization
    context_object_name = "organizations"
    template_name = "home.html"
    paginate_by = 10

    def get_queryset(self):
        return Organization.objects.all().order_by("-created_at")


class OrganizationList(ListView):
    model = Organization
    context_object_name = "object_list"
    template_name = "org_list.html"
    paginate_by = 5


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "org_del.html"
    success_url = reverse_lazy("organization-list")