from django.urls import path
from . import views
urlpatterns = [
    path('',views.BlogPageView.as_view(),name='home'),
    path('details/<slug:slug>',views.BlogDetailView.as_view(),name='post_detail'),
    path('update/<slug:slug>',views.BlogUpdateView.as_view(),name='post_update'),
    path('delete/<slug:slug>',views.BlogDeleteView.as_view(),name='post_delete'),
    path('create/new/',views.BlogCreateView.as_view(),name='create_blog')
]
