from django.urls import path
from .views import home, LinktreeListView, LinkButtonListCreateView

urlpatterns = [
    path("",  home),
    path("linktree_list", LinktreeListView.as_view()),
    path("button_list", LinkButtonListCreateView.as_view()),
]
