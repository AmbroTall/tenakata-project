from django.urls import path
from .views import home_page, RegistrationView, admit_list_view, delete_register, UpdateView
# from .views import home_page, RegistrationView, AdminListView

app_name = 'tenakata'

urlpatterns = [
    path('', home_page, name="homepage"),
    path('register/', RegistrationView.as_view(), name="register_page"),
    path('list/', admit_list_view, name="list_page"),
    path('update/<int:pk>', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', delete_register, name='delete'),
]