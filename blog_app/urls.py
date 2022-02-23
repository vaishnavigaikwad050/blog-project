from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage.as_view()),
    path('home',views.HomePage.as_view()),
    path('addblog',views.displayform),
    path('add',views.save_fun),
    path('savedata',views.save_fun),
    path('displaydata',views.display_data),
    path('edit/<int:id>',views.edit_blog),
    path('updatedata/<int:id>',views.update_fun),
    path('delete/<int:id>',views.delete_blog),
    path('search',views.search_blog)
]