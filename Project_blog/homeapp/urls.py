
from django.urls import path,include
from .import views

urlpatterns = [
    
    path('',views.index,name='home'),
    path('search/',views.search_result,name='search'),
    path('listdata/',views.ListData.as_view(),name='listdata'),
    path('detaildata/<int:pk>',views.DetailData.as_view(),name='detaildata'),
    path('editdata/<int:pk>',views.EditBlog.as_view(),name='editblog'),
    path('deleteblog/<int:pk>/remove',views.DeleteBlog.as_view(),name='deleteblog'),
]