from django.conf.urls import url
from . import views
from django.urls import path
from journal import views

app_name = 'journal'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('resources/new/', views.ResourceCreateView.as_view(), name='resource-add'),
    path('resources/update/<int:pk>', views.ResourceUpdateView.as_view(), name='resource-update'),
    path('resources/delete/<int:pk>', views.ResourceDeleteView.as_view(), name='resource-delete'),
    path('softwares/add', views.SoftwareCreateView.as_view(), name='software-add'),
    path('tetris', views.tetris, name='tetris'),
]

