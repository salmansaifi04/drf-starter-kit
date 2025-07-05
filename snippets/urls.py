from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('fbsnippets/', views.fbsnippet_list),
    path('fbsnippets/<int:pk>/', views.fbsnippet_detail),
    path('cbsnippets/', views.CBsnippet_list.as_view()),
    path('cbsnippets/<int:pk>', views.CBsnippet_detail.as_view()),
    path('mgcbsnippets/', views.MGCB_snippet_list.as_view()),
    path('mgcbsnippets/<int:pk>', views.MGCB_snippet_detail.as_view()),
    path('gcbsnippets/', views.GCB_snippet_list.as_view()),
    path('gcbsnippets/<int:pk>', views.GCB_snippet_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
