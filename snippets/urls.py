from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('fbsnippets/', views.fbsnippet_list),
    path('fbsnippets/<int:pk>/', views.fbsnippet_detail)
]


urlpatterns = format_suffix_patterns(urlpatterns)
