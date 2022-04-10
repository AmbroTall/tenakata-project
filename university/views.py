from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import RegistrationForm
from django.contrib.messages.views import SuccessMessageMixin
from .models import Registration
import datetime


# Homepage View.
def home_page(request):
    return render(request, "university/home.html")


# Registration View
class RegistrationView(CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'university/register_form.html'
    success_url = reverse_lazy("tenakata:list_page")





#
#
# def RegistrationView(request):
#     error = ""
#     if request.method == "POST":
#         registration_form = RegistrationForm(data = request.POST)
#         if registration_form.is_valid():
#             student = registration_form.save(commit=False)
#             if student.age < 1:
#
#         else:
#             error = 'form error'
#     else:
#         registration_form = RegistrationForm()
#     context = {
#         'error': error,
#         'registration_form': registration_form
#     }
#     return render(request, 'university/register_form.html', context)


# Admission Edit View
class UpdateView(UpdateView):
    model = Registration
    template_name = 'university/update_view.html'
    fields = '__all__'
    success_url = reverse_lazy('tenakata:list_page')


# All registered student view
def admit_list_view(request):
    names = Registration.objects.all()
    admissibility = []
    lists = []
    age = []
    gender = []
    others = []
    unqualified = []
    for name in names:
        if name.age >= 43 and name.iq_test > 100 and name.gender == 'female':
            age.insert(0, name)

        elif name.age >= 43 and name.iq_test > 100 and name.gender == 'male':
            age.insert(-1, name)

        elif name.age >= 26 and name.iq_test > 100 and name.gender == 'female':
            gender.insert(0, name)

        elif name.age >= 26 and name.iq_test > 100 and name.gender == 'male':
            gender.insert(-1, name)

        elif name.age < 26 and name.iq_test > 100 and name.gender == 'female':
            others.insert(0,name)

        elif name.age < 26 and name.iq_test > 100 and name.gender == 'male':
            others.append(name)
        else:
            unqualified.append(name)

    lists.append(age)
    lists.append(gender)
    lists.append(others)

    for list in lists:
        for name in list:
            admissibility.append(name)

    context = {
        'admissibility':admissibility
    }
    return render(request, 'university/admit_list.html', context)


# Delete Student View
def delete_register(request, pk=None):
    Registration.objects.filter(id=pk).delete()
    return redirect('tenakata:list_page')